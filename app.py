import os, glob
from sys import platform
from flask import Flask, render_template, send_file, request
from flask_paginate import Pagination, get_page_parameter
from whitenoise import WhiteNoise
from readabilipy import simple_json_from_html_string
from config import *


app = Flask(__name__)
app.wsgi_app = WhiteNoise(app.wsgi_app)

# Note: It could be possible to add more than one directory, 
# but you have to adjust the code accordingly in the get_filenames function
my_static_folders = (
    SAVED_WEBPAGES_DIR,
    # "static/folder/two/",
    # "static/folder/three/",
)
for static in my_static_folders:
    app.wsgi_app.add_files(static)


'''
Renders the index of the site
'''
@app.route("/")
def index():
    file_list = get_filenames()
    files = [ file.split('/')[-1] for file in file_list]
    page = request.args.get(get_page_parameter(), type=int, default=1)
    pagination, page_files = get_pagination(page, files)
    return render_template('index.html', files=page_files, pagination=pagination)


'''
Return the pagination object and the list of the filenames of the current page
'''
def get_pagination(page, files):
    per_page = PER_PAGE
    pagination = Pagination(page=page, total=len(files), search=False, record_name='files', per_page=per_page)
    page_files = files[(page-1) * per_page : ((page-1) * per_page)+per_page]
    return (pagination, page_files)


'''
Send the file without processing to the browser
'''
@app.route('/file/<filename>')
def file(filename):
    file = SAVED_WEBPAGES_DIR + filename
    return send_file(file)


'''
Displays the file in a more friendly way to read
It uses Mozilla Readability library if possible
'''
@app.route('/read/<filename>')
def read(filename):
    if filename.split('.')[-1].lower() in READ_MODE_FILES_COMPATIBLE:
        file = SAVED_WEBPAGES_DIR + filename
        article = {}
        with open(file, 'r') as document:
            text = document.read()
            article = simple_json_from_html_string(text, use_readability=USE_READABILITY)
        title = article.get('title') if article.get('title') else filename.split('.')[-2]
        content = txt2html(text) if filename.split('.')[-1].lower() != 'html' else article.get('content')
        return render_template('read.html', content=content, title=title)
    return "<p style='font-size:2em;'>File not compatible with Read Mode</p>"

'''
Filter the files by filename searching one o more words
'''
@app.route('/search', methods=['GET'])
def search():
    search_words = request.args.get('query', '')
    search_words = str(search_words).lower().split(' ')
    file_list = get_filenames()
    filtered_list = [s for s in file_list if all(xs in s.lower() for xs in search_words)]
    files = [ file.split('/')[-1] for file in filtered_list]
    page = request.args.get(get_page_parameter(), type=int, default=1)
    pagination, page_files = get_pagination(page, files)
    return render_template('search.html', 
                            files=page_files,
                             pagination=pagination, 
                             query=request.args.get('query', '')\
        )


'''
Return the filenames in the order selected in the config file
'''
def get_filenames():
    file_list = []
    for type in FILE_TYPES_ALLOWED:
        file_list.extend(glob.glob(SAVED_WEBPAGES_DIR + '*.' + type))
        if platform == 'linux' or platform == 'linux2':
            file_list.extend(glob.glob(SAVED_WEBPAGES_DIR + '*.' + type.upper()))
    if SORT_BY == 'CREATION':
        file_list.sort(key=os.path.getctime, reverse=REVERSE_ORDER)
    elif SORT_BY == 'MODIFIED':
        file_list.sort(key=os.path.getmtime, reverse=REVERSE_ORDER)
    else:
        file_list.sort(reverse=REVERSE_ORDER)
    return file_list

# It actually do not convert to html
# but adding <p> tags is enough to display text correctly  in the Kindle
def txt2html(text):
    paragraphs = text.split('\n')
    output = ''
    for para in paragraphs:
        output += '<p>' + para + '</p>'
    return output