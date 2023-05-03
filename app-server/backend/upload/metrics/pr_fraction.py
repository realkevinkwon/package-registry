import subprocess
import json
import sys
import os, shutil
from .valid_url import *
from .pull_req_graphql import *
import git
import re

token = os.getenv("GITHUB_TOKEN")

def pull_request_fraction(url, owner_repo):
    
    # Creates Local Repo Folder if non-existing, else remove it
    path = "Repo-Analysis"
    if(os.path.isdir(path)):
        shutil.rmtree(path)
    
    # Clones the Repository Locally inside the Path folder
    git.Repo.clone_from(url, path)

    # Run and store cloc data to json file
    with open('cloc_files.json', 'w') as f:
        subprocess.check_call(['cloc', '--by-file', '--json', path], stdout=f)
    cloc_json = open('cloc_files.json')
    cloc_data = json.load(cloc_json)
    
    list_of_files = []
    filename_regex = r"/([^/]+)$" # Regex function to get file name from path

    # Get Total Lines of Code and list of analyzed files
    for item in cloc_data:
        match = re.search(filename_regex, item)  # Regex function used to check if there is a path to a file
        if match:
            match_filename = item.replace("Repo-Analysis/", "")
            list_of_files.append(match_filename)
        elif(item == 'SUM'):
            total_lines = int(cloc_data[item]['code'])
                
    # Make GraphQL Call for PR Fraction
    pr_total_lines = pr_fraction_gql(owner_repo, list_of_files, token)

    # Get total lines of code in Repository
    score = round(float(pr_total_lines)/float(total_lines), 2)
    
    # After using Git Repo, delete the Folder
    if(os.path.isdir(path)):
        shutil.rmtree(path)
    return score

def pr_score(url):
    
    # Regex the Package name and get the Github Owner and Repo
    if(url.__contains__("npmjs")):
        package_name = re.search(r"/package/([\w-]+)", url).group(1)
        owner_repo = str(npm_to_git(package_name))[1:]
        url = f"https://github.com/{owner_repo}"
    else:
        owner_repo = url.replace("https://github.com/", "")

    # Checks if valid url, and then calls score function
    if (valid_url(url)):
        score = pull_request_fraction(url, owner_repo)
    return score