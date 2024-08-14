import os

import requests
import json

import ctypes

application_dir = os.path.dirname(__file__)

# command line utility



# connection to nasa's APOD API


# TODO: implement proper key checking
key = os.environ.get("apod-key")

environment = "prod" #os.environ.get("bntu-state")

if key == None:
    print("bad key")

if environment != "prod":
    mockfile = open(application_dir + '\mock.json')
    result = json.load(mockfile)
else:
    response = requests.get(f"https://api.nasa.gov/planetary/apod?api_key={key}")
    result = json.loads(response.text)

print(result)

image = requests.get(result["url"],stream=True)

file_type = result["url"].split(".")[-1]

if image.status_code == 200:
    with open(f"test.{file_type}",'wb') as output:
        for chunk in image:
            output.write(chunk)

    ctypes.windll.user32.SystemParametersInfoW(20, 0, f"{application_dir}/test.{file_type}" , 0)
else:
    print(f"failed to load image with status code: {image.status_code}")


# find a way to set the desktop background to that file


#TODO: remove this
print("program finished")