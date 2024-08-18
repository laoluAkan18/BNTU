import os

import requests
import json

import ctypes
import winreg

application_dir = os.path.dirname(__file__)


#enum to handle windows wallpaper styles
class wallPaperStyle():
    FILL = 10
    FIT = 6
    TILE = -1
    STRETCH = 2
    CENTER = 0
    SPAN = 22


def set_wallpaper_style(style: int) -> bool:
    print(f"style: {style}")
    successful = False

    #location where windows stores the path to the background image
    WINDOWS_REGISTRY_WALLPAPER_STYLE_DIR = "Control Panel\Desktop"

    try:
        print("got here 1")
        
        winreg.CreateKey(winreg.HKEY_CURRENT_USER, WINDOWS_REGISTRY_WALLPAPER_STYLE_DIR)
        print("got here 2")
        registry_key = winreg.OpenKey(winreg.HKEY_CURRENT_USER, WINDOWS_REGISTRY_WALLPAPER_STYLE_DIR, 0, winreg.KEY_WRITE)
        print("got here 3")
        print(registry_key)

        if style == -1:
            print("got here 4")
            winreg.SetValueEx(registry_key, "TileWallpaper",0, winreg.REG_SZ, "1")
            winreg.SetValueEx(registry_key, "WallpaperStyle",0, winreg.REG_SZ, "0")
            print("got here 5")
        else:
            winreg.SetValueEx(registry_key, "TileWallpaper",0, winreg.REG_SZ, "0")
            winreg.SetValueEx(registry_key, "WallpaperStyle",0, winreg.REG_SZ, str(style))

        print("got here 6")
        winreg.CloseKey(registry_key)
        successful = True
    except WindowsError as err:
        print("Error occured")
        print(err)
    print("got here 7")
    return successful
        


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

print(result)

image = requests.get(result["url"],stream=True)

file_type = result["url"].split(".")[-1]

if image.status_code == 200:
    with open(f"test.{file_type}",'wb') as output:
        for chunk in image:
            output.write(chunk)


    print(wallPaperStyle.TILE)
    set_wallpaper_style(wallPaperStyle.CENTER)

    #set desktop background image to the 
    ctypes.windll.user32.SystemParametersInfoW(20, 0, f"{application_dir}/test.{file_type}" , 0)
    
else:
    print(f"failed to load image with status code: {image.status_code}")


# find a way to set the desktop background to that file


#TODO: remove this
print("program finished")