from os import listdir
import re
from PIL import Image

ignoredFiles = ['.DS_Store', 'composite.PNG']

def smartnumbers(n):
    matches = re.findall('\d+', n)
    if 0 == len(matches): return n
    return int(matches[0])

def list_screenshots(directory):
    list = listdir(directory)
    for ignoredFile in ignoredFiles:
        if ignoredFile in list: list.remove(ignoredFile)
    list.sort(key=smartnumbers)
    return list

path = '/Users/ellie/Desktop/ASSets'
myFileNames = list_screenshots(path)

compositeImage = Image.new("RGB", (640, 10000), "white")

n = 0

for fileName in myFileNames:
    screenshotImage = Image.open(path + '/' + fileName)
    compositeImage.paste(screenshotImage, (0, n * 1136))
    n = n + 1

compositeImage.save(path + '/' + "composite.PNG", "PNG")


