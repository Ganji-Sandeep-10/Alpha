import requests
# app.py
from fastapi import  HTTPException
def fetch_files(repo_owner: str, repo_name: str, path: str = "") -> list[dict]:
    """
    Recursively fetch all files from a GitHub repo using the REST API.
    Returns a list of dicts: [{"path": str, "url": str}, ...]
    """
    url = f"https://api.github.com/repos/{repo_owner}/{repo_name}/contents/{path}"
    response = requests.get(url)
    
    if response.status_code != 200:
        raise HTTPException(status_code=response.status_code, detail=response.json())
    
    items = response.json()
    files = []
    for item in items:
        if item["type"] == "file":
            files.append({"path": item["path"], "url": item["download_url"]})
        elif item["type"] == "dir":
            files.extend(fetch_files(repo_owner, repo_name, item["path"]))
    return files