import json

import rainbow as rainbow
from requests_html import HTMLSession
from datetime import date
import os
path = 'text_files'
today = date.today()
# open a (new) file to write
createFile = open(os.path.join(path, f'{today}.txt'), "w")
createFile.close()

# open a read and append version so I can compare and add new headlines
readFile = open(os.path.join(path, f'{today}.txt'), "r")
appendFile = open(os.path.join(path, f'{today}.txt'), "a")

readFile =readFile.read()
# print(readFile)

url = 'https://news.google.com/rss/'
# url = 'https://news.google.com/rss/search?q=political'
list = []
s = HTMLSession()

r = s.get(url)

for title in r.html.find('title'):
    title = str(title.text)
    list.append(title)
    if title not in readFile:
        appendFile.write(f'{title}\n')



#
# from PIL import Image
# from pythonWordArt import pyWordArt
# w = pyWordArt()
# w.WordArt(str(my_file), w.Styles[mystyle], "100")
# pil_im = Image.open(w.toBufferIO())
# pil_im.show()

