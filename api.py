print('Start api read application')

import requests

#comment 
url = requests.get("https://catfact.ninja/facts")
print(url)

facts = url.json()
print(facts["data"][0])