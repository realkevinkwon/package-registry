import json
import os
import shutil
import subprocess
from sys import argv
import requests
import re
# from dotenv import load_dotenv

# load_dotenv()


def getRampUpScore(link):
    if "npmjs.com" in link:
        npm_reg_link = "https://registry." + \
            link.split("www.")[1].replace("/package", '')
        response = requests.get(npm_reg_link)
        result = response.json()
        githubLink = result["repository"]["url"].split("github.com")[
            1].split("/")
        repo_url = "https://github.com" + \
            result["repository"]["url"].split("github.com")[1]
    elif "github.com" in link:
        repo_url = link
    else:
        return "URLs from this organization are not supported currently."

    repo_dir = (repo_url.split("github.com")[
                1].split("/"))[2].replace(".git", "")
    print(repo_url)
    print(repo_dir)

    # Clone the repository
    subprocess.run(["git", "clone", repo_url, repo_dir], check=True)
    # Change the current working directory to the repository
    os.chdir(repo_dir)

    # Open the README file
    try:
        with open("README.md", "r") as file:
            lines = file.readlines()
    except FileNotFoundError:
        try:
            with open("README.markdown", "r") as file:
                lines = file.readlines()
        except FileNotFoundError:
            total_score = 0
            return
    file.close()
    install_section = 0
    usage_section = 0
    examples_section = 0
    docs_section = 0
    # Search README for helpful sections
    for line in lines:
        if re.match(r"#+ *install(ation)?", line, re.IGNORECASE):
            install_section = 1
        if re.match(r"#+ *Usage", line, re.IGNORECASE) or re.match(r"#+ *Examples", line, re.IGNORECASE):
            usage_section = 1
        if re.match(r"#+ *Doc(umentation)?", line, re.IGNORECASE):
            docs_section = 1

    readmeSectionScore = (install_section + usage_section + docs_section) / 3
    readmeLengthScore = 0
    readmeLineCount = len(lines)
    if readmeLineCount > 150:  # decide on better metrics
        readmeLengthScore = 1
    elif readmeLineCount < 150 and readmeLineCount > 125:
        readmeLengthScore = 0.9
    elif readmeLineCount < 125 and readmeLineCount > 100:
        readmeLengthScore = 0.8
    elif readmeLineCount < 30 and readmeLineCount > 0:
        readmeLengthScore = 0
    else:
        readmeLengthScore = readmeLineCount/100 * 0.8

    # print("Section Score: "+str(readmeSectionScore))
    # print("Length Score: "+str(readmeLengthScore) +
    #       "  Length: " + str(readmeLineCount))
    total_score = round((readmeLengthScore + readmeSectionScore)/2, 2)

    print("RampUp Score: " + str(total_score))
    os.chdir("..")

    # Delete the repository directory
    full_dir = os.path.join(os.getcwd(), repo_dir)

    subprocess.run(["rm", "-rf", full_dir], check=True)
    return(total_score)

if __name__ == "__main__":
    getRampUpScore(str(argv[1]))