import requests

def fetch_files(repo_owner: str, repo_name: str, path: str = "") -> list[dict]:
    """
    Recursively fetch all files from a GitHub repo using the REST API.
    
    Returns:
        A list of dicts: [{"path": str, "url": str}, ...]
    """
    url = f"https://api.github.com/repos/{repo_owner}/{repo_name}/contents/{path}"
    response = requests.get(url)
    response.raise_for_status()
    items = response.json()
    files = []
    for item in items:
        if item["type"] == "file":
            files.append({"path": item["path"], "url": item["download_url"]})
        elif item["type"] == "dir":
            files.extend(fetch_files(repo_owner, repo_name, item["path"]))
    return files

# Example usage (no print, just data return)
repo_files = fetch_files("Ganji-Sandeep-10", "ToDo-List")

# repo_files is now a list like:
# [
#   {"path": ".eslintrc.json", "url": "https://..."},
#   {"path": "src/App.js", "url": "https://..."},
#   {"path": "public/index.html", "url": "https://..."},
#   ...
# ]
