from datetime import datetime
from sys import argv
import requests
import json
import dotenv
import os

dotenv.load_dotenv()

# Constants for time intervals in seconds
MONTH_IN_SECONDS = 60 * 60 * 24 * 30
WEEK_IN_SECONDS = 60 * 60 * 24 * 7
GITHUB_TOKEN = os.getenv("GITHUB_TOKEN")  # Replace with actual Github token if available

# Function to calculate the responsive score of a Github repository
def getResponsiveScore(link, outfile):
    if "npmjs.com" in link:
        npm_reg_link = "https://registry." + link.split("www.")[1].replace("/package",'')
        response = requests.get(npm_reg_link)
        result = response.json()
        githubLink = result["repository"]["url"].split("github.com")[1].split("/")
    elif "github.com" in link:
        githubLink = link.split("github.com")[1].split("/")
    else:
        return "URLs from this organization are not supported currently."

    owner = githubLink[1]
    repo = githubLink[2].replace(".git", "")

    # Make a request to the Github API to get the repository details
    repoAPI_link = "https://api.github.com/repos" + "/{}/{}".format(owner, repo)
    response = requests.get(repoAPI_link, headers={'Authorization': "token {}".format(GITHUB_TOKEN)})
    result = response.json()

    # Get the list of last 100 commits to the repository
    commitsURL = result["commits_url"].replace("{/sha}", "")
    response = requests.get(commitsURL + "?per_page=100", headers={'Authorization': "token {}".format(GITHUB_TOKEN)})
    lastHundredCommits = response.json()

    # Get the list of closed issues in the repository
    issuesURL = result["issues_url"].replace("{/number}", "")
    response = requests.get(issuesURL + "?state=closed&per_page=100", headers={'Authorization': "token {}".format(GITHUB_TOKEN)})
    issues = response.json()

    # Calculate the number of commits and closed issues
    numIssues = len(issues)
    numCommits = len(lastHundredCommits)

    # Calculate the average time between commits
    commitTimeSum = 0
    for i in range(1, len(lastHundredCommits)):
        current = lastHundredCommits[i]["commit"]["committer"]["date"]
        current = datetime.strptime(current, '%Y-%m-%dT%H:%M:%SZ').timestamp()
        prev = lastHundredCommits[i - 1]["commit"]["committer"]["date"]
        prev = datetime.strptime(prev, '%Y-%m-%dT%H:%M:%SZ').timestamp()
        commitTimeSum += prev - current
        
    lastCommit = datetime.strptime(lastHundredCommits[0]["commit"]["committer"]["date"], '%Y-%m-%dT%H:%M:%SZ').timestamp()
    currentTime = datetime.now().timestamp()

    if (currentTime - lastCommit) <= MONTH_IN_SECONDS: 
        last_commit_ratio = 1
    else:
        scaled_ratio = 1 - ((currentTime - lastCommit) - (30 * 24 * 60 * 60)) / (365 * 24 * 60 * 60) # 365 days in a year
        last_commit_ratio =  max(0, min(1, scaled_ratio))

    # Calculate the average time to close an issue
    issueCloseSum = 0
    for issue in issues:
        createdAt = issue["created_at"]
        closedAt = issue["closed_at"]
        openDate = datetime.strptime(createdAt, '%Y-%m-%dT%H:%M:%SZ').timestamp()
        closeDate = datetime.strptime(closedAt, '%Y-%m-%dT%H:%M:%SZ').timestamp()
        issueCloseSum += closeDate-openDate
    
    # accounting for numIssuses = 0, setting it to 1 to avoid division by 0
    if numIssues == 0:
        numIssues = 1
    if numCommits == 0:
        numCommits = 1
    averageCloseTime = issueCloseSum / numIssues
    commitFrequency = (commitTimeSum) / numCommits

    issueCloseScore = 0

    if commitFrequency < 2*WEEK_IN_SECONDS:
        commitFrequencyScore = 1
    elif commitFrequency < MONTH_IN_SECONDS and commitFrequency >= 2*WEEK_IN_SECONDS:
        commitFrequencyScore = 0.7
    elif commitFrequency < 3*MONTH_IN_SECONDS and commitFrequency >= MONTH_IN_SECONDS:
        commitFrequencyScore = 0.35
    else:
        commitFrequencyScore = 0
    commitFrequencyScore *= last_commit_ratio

    if averageCloseTime < 0.5*WEEK_IN_SECONDS:
        issueCloseScore = 1
    elif averageCloseTime < 0.5*MONTH_IN_SECONDS and averageCloseTime >= 0.5*WEEK_IN_SECONDS:
        issueCloseScore = 0.7
    elif averageCloseTime < MONTH_IN_SECONDS and averageCloseTime >= 0.5*MONTH_IN_SECONDS:
        issueCloseScore = 0.35
    else:
        issueCloseScore = 0
    # Potential outputs to log file
    # print("Commit Score: " + str(commitFrequencyScore) + "  Average commit time(days):" + str(commitFrequency/60/60/24))
    # print("Issue Score: " + str(issueCloseScore) + "  Avg close time(days):" + str(averageCloseTime / 60 / 60 / 24))
    total_score = round(0.5 * commitFrequencyScore + 0.5 *issueCloseScore, 2)
    # print(total_score)
    print(total_score)
    try:
        with open(outfile, "r") as f:
            data = json.load(f)
            print(data)
    except:
        data = {}

    # Update the score of the "ResponsiveMaintainer" metric
    if link in data:
        data[link]["ResponsiveMaintainer"] = total_score
    else:
        data[link] = {"ResponsiveMaintainer": total_score}

    # Write the updated JSON data back to the file
    with open(outfile, "w") as f:
        json.dump(data, f, indent=4)

    print(total_score)

if __name__ == "__main__":
    getResponsiveScore(str(argv[1]), argv[2])