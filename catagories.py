#
import requests
import json

        


headers = {'Accept-version': '3.0'}
response = requests.get("https://api.reverb.com/api/listings?item_city=Tampa&make=Martin&query=12", headers=headers)


json_obj = json.loads(response.text)

print(json.dumps(json_obj, indent=2))




print(response.status_code)

