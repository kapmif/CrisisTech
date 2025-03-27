import requests
import os

GITHUB_TOKEN = os.getenv('GH_TOKEN')
REPO_OWNER = "kapmif"
REPO_NAME = "CrisisTech"

search_url = "https://api.github.com/search/repositories?q=starlink+billing+hotspot"
headers = {"Authorization": f"token {GITHUB_TOKEN}"}

response = requests.get(search_url, headers=headers)
results = response.json()["items"]

for repo in results[:3]:  # 取前3个结果
    issue_data = {
        "title": f"[Starlink Billing] Found: {repo['name']}",
        "body": f"**Repository**: {repo['html_url']}\n\n**Description**: {repo['description']}",
        "labels": ["starlink", "billing"]
    }
    requests.post(
        f"https://api.github.com/repos/{REPO_OWNER}/{REPO_NAME}/issues",
        json=issue_data,
        headers=headers
    )
