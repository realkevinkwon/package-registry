from datetime import datetime
from sys import argv
import requests
import json
# from dotenv import load_dotenv
import os

# load_dotenv()

GITHUB_TOKEN = os.getenv("GITHUB_TOKEN")

def getCorrectnessScore(link):
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

    repoAPI_link = "https://api.github.com/repos"f"/{owner}/{repo}"
    response = requests.get(repoAPI_link, headers={'Authorization': "token{}".format(GITHUB_TOKEN)})
    result = response.json()
    for i in result:
        print(i, result[i])
    forks_count = result["forks"]

    query = """
    query {
    repository(owner: "OWNER", name: "REPO") {
        issues(states:OPEN, first: 100) {
        totalCount
        edges {
            node {
            title
            labels(first:100) {
                edges {
                node {
                    name
                }
                }
            }
            }
        }
        }
    }
    }
    """
    query = query.replace("OWNER",owner)
    query = query.replace("REPO",repo)

    headers = {
        "Authorization": "Bearer {}".format(GITHUB_TOKEN)
    }

    response = requests.post("https://api.github.com/graphql", json={ "query": query }, headers=headers)
    result = response.json()

    total_issue_count = result["data"]["repository"]["issues"]["totalCount"]
    firstHundredIssues = result["data"]["repository"]["issues"]["edges"]
    actualIssues = 100
    for issue in firstHundredIssues:
        labels = [label["node"]["name"] for label in issue["node"]["labels"]["edges"]]
        if "question" in labels or "awaiting more info" in labels or "discussion" in labels or "awaiting more information" in labels or "discuss" in labels or "invalid" in labels or "duplicate" in labels or "enhancement" in labels:
            actualIssues -= 1
    approx_real_issues = total_issue_count * (actualIssues/100)
    
    
    # accounting for forks_count = 0, setting it to 1 to avoid division by 0
    if forks_count == 0:
        forks_count = 1
    percent_with_errors = approx_real_issues/forks_count * 100
    # print(percent_with_errors)
    issueScore = max(0,1 - percent_with_errors/10)
    issueScore = round(issueScore, 2)
    return(issueScore)
    # try:
    #     with open(outfile, "r") as f:
    #         data = json.load(f)
    # except:
    #     data = {}

    # # Update the score of the "ResponsiveMaintainer" metric
    # if link in data:
    #     data[link]["Correctness"] = issueScore
    # else:
    #     data[link] = {"Correctness": issueScore}

    # # Write the updated JSON data back to the file
    # with open(outfile, "w") as f:
    #     json.dump(data, f, indent=4)


# if __name__ == "__main__":
#     getCorrectnessScore(str(argv[1]), argv[2])
