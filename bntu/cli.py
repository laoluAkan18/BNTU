from bntu import __app_name__, __version__, windows_wallpaper_controller

from typing import Optional

import typer

import platformdirs

import os
import requests
import json

app = typer.Typer()

def _date_callback(value: str) -> None:
    if value:
        
        wallpaper = windows_wallpaper_controller.windows_wallpaper_controller()
        key = os.environ.get("apod-key")

        if key == None:
            raise typer.Abort()

        response = requests.get(f"https://api.nasa.gov/planetary/apod?api_key={key}&date={value}")
        result = json.loads(response.text)

        image = requests.get(result["url"],stream=True)

        file_type = result["url"].split(".")[-1]

        wallpaper_file = platformdirs.user_pictures_dir() + ".\\wallpaper";
        

        #TODO: replace this will a static path using platformsdir package
        with open(f"{wallpaper_file}.{file_type}",'wb') as output:
            for chunk in image:
                output.write(chunk)


        wallpaper.setWallpaper(f"{wallpaper_file}.{file_type}")
        
        print(f"{wallpaper_file}.{file_type}")

        raise typer.Exit()



def _key_callback(value: str) -> None:
    if value:

        wallpaper = windows_wallpaper_controller.windows_wallpaper_controller()

        response = requests.get(f"https://api.nasa.gov/planetary/apod?api_key={value}")
        result = json.loads(response.text)
        print(result)

        image = requests.get(result["url"],stream=True)
        
        if not result["url"]:
            print("invalid api key")
            raise typer.Abort()
        

        file_type = result["url"].split(".")[-1]

        wallpaper_file = platformdirs.user_pictures_dir() + ".\\wallpaper";
        

        #TODO: replace this will a static path using platformsdir package
        with open(f"{wallpaper_file}.{file_type}",'wb') as output:
            for chunk in image:
                output.write(chunk)


        wallpaper.setWallpaper(f"{wallpaper_file}.{file_type}")
        
        print(f"{wallpaper_file}.{file_type}")

    

def _picture_callback(value: str) -> None:
    match value:
        case "":
            pass
        case _:
            pass
    raise typer.Abort()

def _style_callback(value: str) -> None:
    if value:
        wallpaper = windows_wallpaper_controller.windows_wallpaper_controller()
        match value.lower():
            case "tile":
                wallpaper.setWallpaperStyle(windows_wallpaper_controller.windows_wallpaper_controller.TILE)

            case "center":
                wallpaper.setWallpaperStyle(windows_wallpaper_controller.windows_wallpaper_controller.CENTER)

            case "stretch":
                wallpaper.setWallpaperStyle(windows_wallpaper_controller.windows_wallpaper_controller.STRETCH)

            case "fit":
                wallpaper.setWallpaperStyle(windows_wallpaper_controller.windows_wallpaper_controller.FIT)

            case "fill":
                wallpaper.setWallpaperStyle(windows_wallpaper_controller.windows_wallpaper_controller.FILL)

            case "span":
                wallpaper.setWallpaperStyle(windows_wallpaper_controller.windows_wallpaper_controller.SPAN)
     
        wallpaper.setWallpaper(f"C:\\Users\\Alexander's Surface\\projects\\BNTU\\wallpaper.jpg")
        raise typer.Exit()


def _version_callback(value: bool) -> None:
    if value:
        typer.echo(f"{__app_name__}.{__version__}")
        raise typer.Exit()

def _main_callback(value: bool) -> None:
    if value:

        wallpaper = windows_wallpaper_controller.windows_wallpaper_controller()
        key = os.environ.get("apod-key")

        if key == None:
            raise typer.Abort()



        response = requests.get(f"https://api.nasa.gov/planetary/apod?api_key={key}")
        result = json.loads(response.text)

        image = requests.get(result["url"],stream=True)

        file_type = result["url"].split(".")[-1]

        wallpaper_file = platformdirs.user_pictures_dir() + ".\\wallpaper";
        

        #TODO: replace this will a static path using platformsdir package
        with open(f"{wallpaper_file}.{file_type}",'wb') as output:
            for chunk in image:
                output.write(chunk)


        wallpaper.setWallpaper(f"{wallpaper_file}.{file_type}")
        
        print(f"{wallpaper_file}.{file_type}")

        raise typer.Exit()
    
@app.callback()
def main(
    date: Optional[str] = typer.Option(
        None,
        "--date",
        "-d",
        help="use this format \"YYYY-MM-DD\" for date functionality",
        callback=_date_callback,
        is_eager=False
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
        is_eager=False
    )
) -> None: return
