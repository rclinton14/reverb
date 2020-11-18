#
#
#
import requests
import json

make = ""
city = ""
headers = {'Accept-version': '3.0'}

while make != 'quit':
    # Ask the user for make and city.
    make = input("Enter Make, or 'quit': ")
    city = input("Enter City: ")
    response = requests.get("https://api.reverb.com/api/listings?item_city="+city,"&make="+make, headers=headers)
    json_obj = json.loads(response.text)

    for listing in json_obj ["listings"]:
        print (listing["make"],"  $",listing["price"]["amount"]," \t",listing["model"])

    #print(response.status_code)
    #print(json.dumps(json_obj, indent=2))
