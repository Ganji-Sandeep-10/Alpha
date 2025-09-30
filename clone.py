import git  # pip install GitPython

repo_url = "https://github.com/Ganji-Sandeep-10/ToDo-List.git"
local_dir = "./repo_clone2"

git.Repo.clone_from(repo_url, local_dir)
print("Repo cloned successfully!")


import os

for root, _, files in os.walk(local_dir):
    for f in files:
        print(os.path.join(root, f))
