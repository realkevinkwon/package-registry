import requests

def pr_fraction_gql(owner_repo, list_of_files, token):
  
  # Get Owner and Repo Separated
  owner_repo_list = owner_repo.split("/")
  owner, repo = owner_repo_list[0], owner_repo_list[1]
  
  # Pagination and File variables
  page_size = 100
  end_cursor = None
  has_next_page = True
  additions = 0
  deletions = 0

  # Loop through pages of results until no more pages
  while has_next_page:
    # GraphQL query
      query = """
      query($owner: String!, $name: String!, $pageSize: Int!, $endCursor: String) {
        repository(owner: $owner, name: $name) {
          pullRequests(states: MERGED, first: $pageSize, after: $endCursor, orderBy: {field: CREATED_AT, direction: ASC}) {
            nodes {
              number
              files(first: 100) {
                nodes {
                  path
                  additions
                  deletions
                }
              }
            }
            pageInfo {
              endCursor
              hasNextPage
            }
          }
        }
      }
      """
      
      # Query Variables
      variables = {
          "owner": owner,
          "name": repo,
          "pageSize": page_size,
          "endCursor": end_cursor
      }
      
      headers = {"Authorization": "Bearer {}".format(token)}
      
      # Execute query and retrieve results
      result = requests.post("https://api.github.com/graphql", json={ "query": query, "variables": variables }, headers=headers)

      # If data is not in this format, skip the Pull Request
      try:
        data = result.json()["data"]["repository"]["pullRequests"]
      except:
        data = None
      
      if data is not None:
        # Loop through nodes and append file data to results list
        for node in data["nodes"]:
            for file in node["files"]["nodes"]:
                if(file["path"] in list_of_files): # Only add files that were counted by Cloc
                  additions += int(file["additions"])
                  deletions += int(file["deletions"])
      
      # Check if there are more pages
      has_next_page = data["pageInfo"]["hasNextPage"]
      if has_next_page:
          end_cursor = data["pageInfo"]["endCursor"]
  
  total_lines = additions - deletions
  
  return total_lines