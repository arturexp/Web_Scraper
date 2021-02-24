import requests
import json

url = input("Input the URL:\n")
r = requests.get(url)
content = json.loads(r.text)
if r.status_code != 200:
    print("Invalid quote resource!")
elif "content" in content:
    print(content["content"])
else:
    print("Invalid quote resource!")

