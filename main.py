import json

import rainbow as rainbow
from requests_html import HTMLSession

# open a (new) file to write
outF = open("data.txt", "w")

url = 'https://news.google.com/rss/'
# url = 'https://news.google.com/rss/search?q=political'

s = HTMLSession()

r = s.get(url)

for title in r.html.find('title'):
    title = str(title.text)
    # print(title)
    outF.write(title)
    outF.write("\n")
outF.close()



my_file = open("data.txt", "r")
content = my_file.read()
content_list = content.split("\n")
# content_list = my_file.readlines()
# my_file.close()
print(content_list)




from PIL import Image
from pythonWordArt import pyWordArt
w = pyWordArt()
w.WordArt(str(my_file), w.Styles[mystyle], "100")
pil_im = Image.open(w.toBufferIO())
pil_im.show()