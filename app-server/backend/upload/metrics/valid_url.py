########################################################################
# Check if the url is valid
# transform the url to correct api call format
# and return the url to a output file
# command line: python3 valid_url.py <input_file> <output_file>
########################################################################

# import 
import sys
import re

def valid_url(url):
    # check if the url is valid with regex
    ## we want to match the following format:
    ## https://github.com/?/?
    ## https://www.npmjs.com/? 
    
    _re = r"https://(github.com|www.npmjs.com)/[a-zA-Z0-9_-]+/[a-zA-Z0-9_-]+"
    
    if re.search(_re, url):
        return True
    
    return False

def get_api_url(url):
    # transform the url to the correct api call format
    
    ## github url format:
    ## api.github.com/repos/?/?
    if url.__contains__("github.com"):
        url = url.replace("github.com", "api.github.com/repos")
        return url
        
    ## npm url format:
    ## registry.npmjs.org/?/
    if url.__contains__("npmjs.com"):
        url = url.replace("www.npmjs.com/package", "registry.npmjs.org")
        return url
    
    return None
        
    

# if __name__ == "__main__":
#     # get the input and output file
#     infile = sys.argv[1]
#     outfile = sys.argv[2]
    
#     # open the input file
#     infile = open(infile, "r")
    
#     # open the output file
#     outfile = open(outfile, "w")
    
#     # urls to be written to the output file
#     for line in infile:
#         url = line.strip()
#         if valid_url(url):
#             # transform the url to the correct api call format
#             # and write it to the output file
#             api_url = get_api_url(url)
#             outfile.write(api_url + "\n")
            