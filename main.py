from os import listdir
import re
from PIL import Image

iOSHeader = 129 # this is the sizing of the header to be removed

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

path = '/Users/ellie/Desktop/images'
myFileNames = list_screenshots(path)

firstImage = Image.open(path + '/' + myFileNames[0])
(width, height) = firstImage.size

compositeImage = Image.new("RGB", (width, len(myFileNames) * height), "red")

pixelsDown = 0

for fileName in myFileNames:
    screenshotImage = Image.open(path + '/' + fileName)
    if pixelsDown > 0:
        screenshotImage = screenshotImage.crop((0, iOSHeader, width, height))
        compositeImage.paste(screenshotImage, (0, pixelsDown))
        pixelsDown = pixelsDown + height - iOSHeader
    else:
        compositeImage.paste(screenshotImage, (0, 0))
        pixelsDown = height

compositeImage = compositeImage.crop((0, 0, width, pixelsDown))
compositeImage.save(path + '/' + "composite.PNG", "PNG")