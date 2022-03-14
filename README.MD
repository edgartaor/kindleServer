# WebServer for Kindle

I save articles to HTML files with  [TagSpaces](https://github.com/tagspaces/browser-extensions) or [SingleFile](https://github.com/gildas-lormeau/SingleFile) to read them later but I could not find a way to serve them easily to a Kindle Paperwhite and read them there. 

This project serve HTML files (and few more) saved in your computer with a UI suitable for Kindle web browser. On top of that, it include a Read Mode (thanks to [ReadabiliPy](https://github.com/alan-turing-institute/ReadabiliPy))  to display the text in a comfortable size without have to use the 'Article Mode' in Kindle web browser.

This app does not use Javascript or any database (the files themselves are the database). To serve the file it uses [Whitenoise](https://whitenoise.evans.io/en/stable/#), so it does not need a nginx o apache server.

*Disclaimer*: I use this app only accesible in my LAN, running
`flask run -h 192.168.1.100 -p 8000` is enough for my use case. If  you need a public instance over the Internet, please setup a proper web server.



