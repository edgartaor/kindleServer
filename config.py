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


# You can also customize the font size, font family and any aspect in the templete files