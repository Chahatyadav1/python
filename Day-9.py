import sys
import requests
import os
name=sys.argv[1]
import collections
count=collections.Counter()
token = os.getenv("GITHUB_TOKEN")
headers={
    "Authentication": f"Bearer {token}",
    "Accept": "application/vnd.github+json",
}
size=0
max_repo=""
repos=requests.get(f"https://api.github.com/users/{name}/repos",headers=headers)
for i in repos.json():
    print(f'{i["name"]:<40}\t{i["forks"]:<10}\t{str(i["language"]):<20}\t{i["open_issues"]:<20}')
    count[i["language"]]+=1
    if size < i["size"]:
        size=i["size"]
        max_repo=i["name"]
print(count.most_common(1)[0][0])
print(max_repo,size)