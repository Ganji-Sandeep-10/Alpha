# app.py
from fastapi import FastAPI, HTTPException
app = FastAPI(title="GitHub Repo File Fetcher")
from test import fetch_files
@app.get("/repo-files/")
async def get_repo_files(owner: str, repo: str):
    """
    Endpoint to fetch all files from a GitHub repo.
    Example: /repo-files/?owner=Ganji-Sandeep-10&repo=ToDo-List
    """
    try:
        files = fetch_files(owner, repo)
        return {"owner": owner, "repo": repo, "files": files}
    except HTTPException as e:
        raise e
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))