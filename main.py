import requests

reqUrl = "https://api.github.com/octocat&quot;

headersList = {
 "Accept": "application/vnd.github+json",
 "User-Agent": "Thunder Client (https://www.thunderclient.com)&quot;,
 "X-GitHub-Api-Version": "2022-11-28"
}

payload = ""

response = requests.request("GET", reqUrl, data=payload,  headers=headersList)

print(response.text)