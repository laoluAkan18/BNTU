import os

import requests
import json

import ctypes
import winreg

application_dir = os.path.dirname(__file__)

FILE_NAME_WORKING = "working"
FILE_NAME_CURRENT = "current"

class WindowsWallpaperController():
    """ Simple class that wraps the windows registry you to change the background image on windows """
    TILE = -1
    CENTER = 0
    STRETCH = 2
    FIT = 6
    FILL = 10
    SPAN = 22
    
    registry_subdir = "Control Panel\Desktop"

    def setWallpaper(self, location:str) -> None:
        """ 
        Update the location the windows ini file points to instantly updating the background image,
        then saves the changes to the registry for persistance.
        """
        
        ctypes.windll.user32.SystemParametersInfoW(20, 0, location , 0)

        try:
            winreg.OpenKey(winreg.HKEY_CURRENT_USER, self.registry_subdir)
            registry_key = winreg.OpenKey(winreg.HKEY_CURRENT_USER, self.registry_subdir, 0, winreg.KEY_WRITE)
            winreg.SetValueEx(registry_key, "Wallpaper",0, winreg.REG_SZ, location)
        finally:
            #if the registry key is currently open, no matter if the background was changed or not, close the key
            if registry_key:
                winreg.CloseKey(registry_key)
        

    def setWallpaperStyle(self, style:int) -> None:
        """
        Update the wallpaper style in the registry 

        NOTE: to update Wallpaper style setWallpaper() must be called.
        """
        
        try:
            registry_key = winreg.CreateKey(winreg.HKEY_CURRENT_USER, self.registry_subdir)
        
            if style == self.TILE:
                winreg.SetValueEx(registry_key, "TileWallpaper",0, winreg.REG_SZ, "1")
                winreg.SetValueEx(registry_key, "WallpaperStyle",0, winreg.REG_SZ, "0")
            else:
                winreg.SetValueEx(registry_key, "TileWallpaper",0, winreg.REG_SZ, "0")
                winreg.SetValueEx(registry_key, "WallpaperStyle",0, winreg.REG_SZ, str(style))
        
        finally:
            #if the registry key is currently open, no matter if the background was changed or not, close the key
            if registry_key:
                winreg.CloseKey(registry_key)




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