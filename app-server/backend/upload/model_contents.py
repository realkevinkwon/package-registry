import requests

# This function set should allow for the extraction of name and popularity scoring

def getModelContents(link):
    # Appropriated from Team 9's method of URL cleaning (acquired from ramp_up.py)
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
        return ["Incompatible Link",-2]
    repo = (repo_url.split("github.com/")[
                    1].split("/"))
    repo_auth = repo[0]
    repo_name = repo[1].replace(".git", "") # Will be used for the repository name (first entry for model)
    repo_dir = repo_auth + "/" + repo_name

    # Go to funcs for individual score and version
    pop_score = getPopularity(repo_dir)
    to_model = [repo_name, pop_score]

def getPopularity(repo_dir):
    url = "https://api.github.com/repos/"+repo_dir+"/releases"
    try: get_contents = requests.get(url)
    except: return 0
    json_contents = get_contents.json()
    downloads_count = 0
    for version in json_contents:
        if "assets" in version:
            if len(version["assets"]) != 0:
                if "download_count" in version["assets"][0]:
                    downloads_count += version["assets"][0]["download_count"]

    url2 = "https://api.github.com/repos/" + repo_dir
    get_stars = requests.get(url2)
    stars_json = get_stars.json()
    if "stargazers_count" in stars_json:
        star_count = stars_json["stargazers_count"]

    if downloads_count > 900000: downloads_count /= 10
    return int(star_count + downloads_count)

def getVersion(repo_dir):
    print("MR BEEEAAASSTT")

if __name__ == '__main__':
    getModelContents("git://github.com/axstin/rbxfpsunlocker.git")
