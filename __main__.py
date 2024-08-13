import os

import requests
import json

application_dir = os.path.dirname(__file__)

# command line utility



# connection to nasa's APOD API


# TODO: implement proper key checking
key = os.environ.get("apod-key")

environment = "prod" #os.environ.get("bntu-state")

if key == None:
    print("bad key")

print(environment == "prod")

if environment != "prod":
    mockfile = open(application_dir + '\mock.json')
    result = json.load(mockfile)
else:
    response = requests.get(f"https://api.nasa.gov/planetary/apod?api_key={key}")
    result = json.load(response.text)

print(result)


# find a way to set the desktop background to that file


#TODO: remove this
print("program finished")