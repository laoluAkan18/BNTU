import ctypes
import winreg

class windows_wallpaper_controller():
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

        except err:
            print(f"error occured: {err}")
        
        finally:
            #if the registry key is currently open, no matter if the background was changed or not, close the 
            if registry_key:
                winreg.CloseKey(registry_key)
