# Bringing NASA To U (BNTU)

This program uses Python to retrieve the [NASA Astronomy Picture Of the Day (APOD)](https://apod.nasa.gov/apod/astropix.html) and enables you to set you background to one of the APOD images once, or daily using windows task scheduler.

The target audience of this project is like-minded developers looking to explore the universe through a CLI tool.

## How the program works

- you specify a directory to store the media of the day

- you run the command to fetch the image from the APOD API

- If there is a network connection the file in the cache directory get overwritten and set as the background

- If there is no network connection specified, then the file in the cache is used as a fallback.

- Sets the background image to the cached image

### Tasks

- Find a way to handle videos when the APOD is not, in fact, a picture.

## The Development

This project was developed using SCRUM methodologies.

For project management we used GITHUB Project.

Weekly SCRUMS on Mondays @ 5:45, and Wednesdays @ 5:45 for 4 weeks.

This project will be built in a docker environment for maximum portability in development.

### Roadmap

- Full implementation of BNTU

- Integration of image upscaler. 