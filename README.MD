# WebServer for Kindle

I save articles into HTML files with  [TagSpaces](https://github.com/tagspaces/browser-extensions) or [SingleFile](https://github.com/gildas-lormeau/SingleFile) to read them later but I could not find a way to serve them easily to a Kindle Paperwhite and read them there. 

This project serve HTML files (and a few more) saved in your computer with a UI suitable for Kindle web browser. On top of that, it include a Read Mode (thanks to [ReadabiliPy](https://github.com/alan-turing-institute/ReadabiliPy))  to display the text in a comfortable size without have to use the 'Article Mode' in Kindle web browser.

This app does not use Javascript or any database (the files themselves are the database). To serve the file it uses [Whitenoise](https://whitenoise.evans.io/en/stable/#), so it does not need a nginx o apache server.

*Disclaimer*: I use this app only accessible in my LAN, running
`flask run -h 192.168.1.100 -p 8000` is enough for my use case. If  you need a public instance over the Internet, please setup a proper web server.

## Demo
https://user-images.githubusercontent.com/430438/158122704-8fe414f9-260e-431d-9d6c-29463062fd7e.mp4

## Install

```bash
git clone https://github.com/edgartaor/kindleServer.git
cd kindleServer
pip install -r requirements.txt
flask run -h 0.0.0.0 -p 8000
```
**Important**: In the `config.py` file change `SAVED_WEBPAGES_DIR` to the path where the HTML files are stored.


## Customize
You can customize some aspects in the `config.py` file. 

```python
# The files that are gonna be listed, 
# compatibility depends on the browser and the device
# Usually if a file it is not compatible in the browser
# it will prompt to download 
# Kindle Paperwhite currently can download .AZW, .PRC and .MOBI with the web browser
# and can display html and txt (pdf is not compatible though)
# other files had not being tested
FILE_TYPES_ALLOWED = ('html', 'txt', 'md', 'pdf', "azw3", "azw",
                        'prc', 'mobi')

# Files that are compatible with the Read Mode
# It support html files and any plain text files
READ_MODE_FILES_COMPATIBLE = ('html', 'txt', 'md')

# Path where the webpages are saved
SAVED_WEBPAGES_DIR = "/mnt/c/Users/Edgar/Documents/Saved webpages/"

# Number of files to show per page
PER_PAGE = 10

# SORT_BY options are 
# 'CREATION' = Creation date
# 'MODIFIED' = Last modification date
# 'FILENAME' = Alphabetical order
SORT_BY = 'CREATION'

# Reverse the order of the files after being sorted
REVERSE_ORDER = True

# Set USE_READABILITY to True if you have a nodejs instance installed
# If mozilla/readability is not found it will fallback to a pure-python parser included in ReadabiliPy
# https://github.com/alan-turing-institute/ReadabiliPy#installation 
USE_READABILITY = True


```

You can also customize the font size, font family and any aspect in the template files

