import requests
import json
import sys
# import numpy as np
# from dotenv import load_dotenv
import os
from .valid_url import *

# load_dotenv()

# GH_token = os.getenv("GITHUB_TOKEN")
GITHUB_TOKEN = "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"

### Compatible Licenses ###
# Sources: https://www.gnu.org/licenses/license-list.en.html and https://spdx.org/licenses/
list_of_licenses = ["LGPL-2.1", "LGPL-2.0", "LGPL-3.0", "GPL-2.0", "GPL-2.1", "	Apache-2.0", "	Artistic-2.0",
                    "ClArtistic", "BSD-3-Clause-LBNL", "BSL-1.0", "BSD-3-Clause", "CECILL-2.0",
                    "CECILL-2.1", "BSD-3-Clause-Clear", "eCos-2.0", "ECL-2.0", "EUDatagrid",
                    "FreeBSD-DOC", "FTL", "HPND", "iMatix", "Imlib2", "	IJG", "Intel", "ISC",
                    "MPL-1.1", "MPL-2.0", "OLDAP-2.7", "Python-2.0", "Ruby", "SMLNJ", "Unicode-TOU",
                    "UPL-1.0", "Unlicense", "Vim", "W3C", "WTFPL", "X11", "Zlib", "ZPL-2.0", "MIT"]
# Compatible Licenses: GPL-2, GPL-2.1, LGPL-2, LGPL-2.1, Apache2.0,
# ArtisticLicense2.0, ClarifiedArtisticLicense, BerkeleyDB, Boost,
# ModifiedBSD, CeCILL2, ClearBSD, eCos2.0, ECL2.0,
# EUDataGrid, Expat, FreeBSD, Freetype, HPND, iMatix, imlib2, IJGL,
# INTEL, ISC, MPL-2.0, MPL-2.1, NCSA, OpenLDAP-2.7, Python2.0,
# Ruby, StandardMLofNJ, Unicode, UPL, Unlicense, Vim, W3C, WTFPL2,
# X11License, ZLib, Zope2.0, MIT


def import_package_github(url, token):
    try:
        # Imports the license dictionary from the URL
        response = requests.get(
            url, headers={'Authorization': f'token {token}'})
        data = response.json()
        license_info = data.get("license", {})

        return -1 if license_info == {} else license_info
    except:
        ### Invalid URL ###
        return -1


def import_package_npmjs(url):
    try:
        # Imports the license dictionary from the URL
        response = requests.get(url)
        data = response.json()
        license_info = data.get("license", "")
        # print(license_info)

        return -1 if license_info == "" else license_info
    except:
        ### Invalid URL ###
        return -1


def calc_license_github(data):
    # if text contains the list of approved licenses for LGPL 2.1, score is 1
    # if not, the score is 0

    if data is not None and data.get("spdx_id") in list_of_licenses:
        return 1
    else:
        return 0


def calc_license_npmjs(data):

    # if text contains the list of approved licenses for LGPL 2.1, score is 1
    # if not, the score is 0

    if isinstance(data, dict):
        license_id = data.get("type")
    elif isinstance(data, str):
        license_id = data
    else:
        license_id = None

    if license_id in list_of_licenses:
        return 1
    else:
        return 0


def score(url, apiurl):
    license_score = 0
    # scores the URLs for license compatibility
    if "github" in apiurl:
        package_data = import_package_github(apiurl, GITHUB_TOKEN)
        # will run if data is imported correctly
        if package_data != -1:
            license_score = calc_license_github(package_data)
        else:
            return(-1)

    elif "npmjs" in apiurl:
        package_data = import_package_npmjs(apiurl)
        # will run if data is imported correctly
        if package_data != -1:
            license_score = calc_license_npmjs(package_data)
        else:
            return(-1)

    # write data to output file
    # try:
    #     with open(jsonfile, "r") as f:
    #         data = json.load(f)
    # except:
    #     data = {}
    # if url in data:
    #     data[url]["License"] = license_score
    # else:
    #     data[url] = {"License": license_score}

    # # Write the updated JSON data back to the file
    # with open(jsonfile, "w") as f:
    #     json.dump(data, f, indent=4)

    print("License: " +str(license_score))
    return(license_score)

def license_score(url):
    if (valid_url(url)):
        apiurl = get_api_url(url)
        return(score(url, apiurl))
    else:
        return -1
        
# if __name__ == "__main__":
#     # sys args are the url and the json file
#     url = sys.argv[1]
#     jsonfile = sys.argv[2]

    # if (vu.valid_url(url)):
    #     apiurl = vu.get_api_url(url)
    #     score(url, apiurl, jsonfile)
