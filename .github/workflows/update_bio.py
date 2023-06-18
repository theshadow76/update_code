import os
from github import Github

# First create a Github instance using an access token
g = Github(os.getenv("GH_TOKEN"))

# Then get your user
user = g.get_user()

# Then loop over all your repositories
total_lines = 0
for repo in user.get_repos():
    # Clone the repo
    os.system(f"git clone {repo.clone_url}")

    # Count the lines of code
    lines = os.popen(f"cloc {repo.name} --include-lang=Python --json").read()
    total_lines += int(lines)

# Update your bio
user.edit(bio=f"I have written {total_lines} lines of code!")
