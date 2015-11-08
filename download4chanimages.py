import urllib.request
import os
import time
from os import walk
from bs4 import BeautifulSoup

url = input("thread to monitor: ")
newpath = input("save folder: ")
element = input("which element are you monitoring?: ")
reference_class = input("what is the class of the element?: ")
monitor = input("monitor? [yes/no]: ")

amount = 0
index = 0

if not os.path.exists(newpath):
    os.makedirs(newpath)

def find_instances(a,f):
    for found in f:
        if a['href'][-17:] == found:
            return 1

def save():
    global amount
    global index
    page = BeautifulSoup(urllib.request.urlopen(url),'html.parser')
    for a in page.find_all(element, {'class': reference_class}):
        amount = amount + 1
    f = []
    for (dirpath, dirnames, filenames) in walk(newpath):
        f.extend(filenames)
        break
    for a in page.find_all(element, {'class': reference_class}):
        if find_instances(a,f) != 1:
            urllib.request.urlretrieve("http:"+a['href'], newpath+"\\"+a['href'][-17:])
            index = index + 1
            print("saved the image:", a['href'], "[",index,"/",amount,"]")
            amount = 0
            return 1

if monitor == "yes":
    while 1 == 1:
        if save() != 1:
            print("nothing new yet")
            time.sleep(5)

else:
    save()
