from bntu import __app_name__, __version__, windows_wallpaper_controller

from typing import Optional

import typer

import platformdirs

import os
import requests
import json

from datetime import datetime

from pathlib import Path

app = typer.Typer()

class application:

    def __init__(self) -> None:
        self._wallpaper_controller = windows_wallpaper_controller.windows_wallpaper_controller()
        self.set_key(f"")
        self.set_date(f"")
        self.set_location(f"")

    def get_key(self) -> str:
        return self._key
    
    def set_key(self,key: str):
        self._key = key
        if key == "":
            self._key = os.environ.get("apod-key")

    def get_date(self) -> str:
        return self._date
    
    def set_date(self,date: str):
        #TODO: implement more date formatting options
        self._date = date

    def get_location(self) -> str:
        return self._location
    
    def set_location(self,location: str):
        self._location = location
        if location == "" or not os.path.isdir(""):
            self._location = platformdirs.user_pictures_dir()

    def get_wallpaper_style(self) -> str:
        pass

    def set_wallpaper_style(self,style: str):
        match style.lower():
            case "tile":
                self._wallpaper_controller.setWallpaperStyle(windows_wallpaper_controller.windows_wallpaper_controller.TILE)

            case "center":
                self._wallpaper_controller.setWallpaperStyle(windows_wallpaper_controller.windows_wallpaper_controller.CENTER)

            case "stretch":
                self._wallpaper_controller.setWallpaperStyle(windows_wallpaper_controller.windows_wallpaper_controller.STRETCH)

            case "fit":
                self._wallpaper_controller.setWallpaperStyle(windows_wallpaper_controller.windows_wallpaper_controller.FIT)

            case "fill":
                self._wallpaper_controller.setWallpaperStyle(windows_wallpaper_controller.windows_wallpaper_controller.FILL)

            case "span":
                self._wallpaper_controller.setWallpaperStyle(windows_wallpaper_controller.windows_wallpaper_controller.SPAN)

    def get_wallpaper(self) -> str:
        return self._wallpaper

    def set_wallpaper(self,location: str):
        self._wallpaper = location

        if self._wallpaper == "" or not os.path.isfile(location):
            self._wallpaper = self.get_location()

        self._wallpaper_controller.setWallpaper(self._wallpaper)


    def fetch_picture(self) -> int:
        print("picture fetched")

        response = requests.get(f"https://api.nasa.gov/planetary/apod?api_key={self.get_key()}&date={self.get_date()}")
        result = json.loads(response.text)


        if "url" not in result:
            print("API could not answer")
            raise typer.Exit()
        
        image = requests.get(result["url"],stream=True)

        file_type = result["url"].split(".")[-1]

        wallpaper_folder = f"{self.get_location()}\\bntu"
        wallpaper_file = f"{wallpaper_folder}\\picture.{file_type}"
        history_file = f"{wallpaper_folder}\\history.txt"

        with open(wallpaper_file,'wb') as output:
            for chunk in image:
                output.write(chunk)

        with open(history_file,'a') as output:
            output.write(datetime.today().strftime('%Y-%m-%d'))

        print(f"{wallpaper_file}")

        self.set_wallpaper(wallpaper_file)
        
        print(f"{wallpaper_file}")
        raise typer.Exit()


bntu_app = application()        

def _key_callback(value: str) -> None:
    if value:
        bntu_app.set_key(value)  

def _picture_callback(value: str) -> None:
    if value:
        bntu_app.set_location(value)

def _style_callback(value: str) -> None:
    if value:
        bntu_app.set_wallpaper_style(value)

def _version_callback(value: bool) -> None:
    if value:
        typer.echo(f"{__app_name__}.{__version__}")
        raise typer.Exit()
    
def _date_callback(value: str) -> None:
    if value:
        bntu_app.set_date(value)

def _main_callback(value: bool) -> None:
    if value:
        bntu_app.fetch_picture()

    
@app.callback()
def main(
    date: Optional[str] = typer.Option(
        None,
        "--date",
        "-d",
        help="use this format \"YYYY-MM-DD\" for date functionality",
        callback=_date_callback,
        is_eager=True
    ),
    version: Optional[bool] = typer.Option(
        None,
        "--version",
        "-v",
        help="Show the application's name and version number",
        callback=_version_callback,
        is_eager=False
    ),
    implementation: Optional[bool] = typer.Option(
        None,
        "--main",
        "-m",
        help="Download todays Astronomy picture of the day",
        callback=_main_callback,
        is_eager=False
    ),
    style: Optional[str] = typer.Option(
        None,
        "--style",
        "-s",
        help="""
        Change the background style, options for windows are:
            TILE
            CENTER
            STRETCH
            FIT
            FILL
            SPAN
        """,
        callback=_style_callback,
        is_eager=True
    ),
    picture: Optional[str] = typer.Option(
        None,
        "--picture",
        "-p",
        help="""
        Save the picture to the provided directory, if no directory is provided, save to default downloads directory.
        """,
        callback=_picture_callback,
        is_eager=False
    ),
    key: Optional[str] = typer.Option(
        None,
        "--key",
        "-k",
        help="""
        manually set the 
        """,
        callback=_key_callback,
        is_eager=True
    )
) -> None: return
