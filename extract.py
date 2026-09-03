import requests
import json
url = "https://dummyjson.com/users"

response = requests.get(url)
response.raise_for_status()
print(response.status_code)

data = response.json()

with open("sales data.json" ,"w") as file:
    json.dump(data,file,indent=4)