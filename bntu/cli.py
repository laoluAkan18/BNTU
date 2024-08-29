from bntu import __app_name__, __version__, windows_wallpaper_controller

from typing import Optional

import typer


app = typer.Typer()


def _version_callback(value: bool) -> None:
    if value:
        typer.echo(f"{__app_name__}.{__version__}")
        raise typer.Exit()
    
@app.callback()
def main(
    version: Optional[bool] = typer.Option(
        None,
        "--version",
        "-v",
        help="Show the application's name and version number",
        callback=_version_callback,
        is_eager=True
    )
) -> None: return