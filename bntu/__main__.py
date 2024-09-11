import os

import requests
import json

import ctypes
import winreg

from bntu import cli, __app_name__, __version__

application_dir = os.path.dirname(__file__)

FILE_NAME_WORKING = "working"
FILE_NAME_CURRENT = "current"

def main():
    cli.app(prog_name=__app_name__)

if __name__ == "__main__":
    main()

"""


# command line utility



# connection to nasa's APOD API


# TODO: implement proper key checking
key = os.environ.get("apod-key")

environment = os.environ.get("bntu-state")

if key == None:
    print("bad key")

if environment != "prod":
    mockfile = open(application_dir + '\mock.json')
    result = json.load(mockfile)
else:
    response = requests.get(f"https://api.nasa.gov/planetary/apod?api_key={key}")
    result = json.loads(response.text)

image = requests.get(result["url"],stream=True)

file_type = result["url"].split(".")[-1]

    

if image.status_code == 200:
    
    #Try downloading the whole image from the server then replace the working one with the current on if successful,
    # if not simply reuse the last working picture
    with open(f"{FILE_NAME_CURRENT}.{file_type}",'wb') as output:
        for chunk in image:
            output.write(chunk)
    


    wallpaperController = WindowsWallpaperController()
    
    wallpaperController.setWallpaperStyle(WindowsWallpaperController.CENTER)
    
    wallpaperController.setWallpaper(f"{application_dir}\\current.{file_type}")

else:
    print(f"failed to load image with status code: {image.status_code}")


wallpaperController = WindowsWallpaperController()

wallpaperController.setWallpaperStyle(WindowsWallpaperController.CENTER)

wallpaperController.setWallpaper(f"{application_dir}\\{FILE_NAME_WORKING}.{fil}")


# find a way to set the desktop background to that file


#TODO: remove this
print("program finished")

"""