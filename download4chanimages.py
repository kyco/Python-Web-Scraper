import urllib.request
import os
import time
from os import walk
from bs4 import BeautifulSoup

url = input("thread to monitor: ")
newpath = input("save folder: ")
monitor = input("monitor? [yes/no]: ")

if not os.path.exists(newpath):
    os.makedirs(newpath)

def find_instances(a,f):
    for found in f:
        if a['href'][-17:] == found:
            return 1

def save():
    page = BeautifulSoup(urllib.request.urlopen(url),'html.parser')
    f = []
    for (dirpath, dirnames, filenames) in walk(newpath):
        f.extend(filenames)
        break
    for a in page.find_all('a', {'class': 'fileThumb'}):
        if find_instances(a,f) != 1:
            urllib.request.urlretrieve("http:"+a['href'], newpath+"\\"+a['href'][-17:])
            print("Found the URL:", a['href'])
            return 1

if monitor == "yes":
    while 1 == 1:
        if save() != 1:
            print("nothing new yet")
            time.sleep(5)
else:
    save()

