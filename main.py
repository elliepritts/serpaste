from os import listdir
import re
from PIL import Image
from PIL import ImageChops

# config variables
path = '/Users/ellie/Desktop/images'
iOSHeader = 129 # this is the height of the iOS header to be removed
overlapStripSize = 60
ignoredFiles = ['.DS_Store', 'composite.PNG']

def smartnumbers(n): # strips anything that is NaN from the filename
    matches = re.findall('\d+', n)
    if 0 == len(matches): return n
    return int(matches[0])

def list_screenshots(directory): # creates an ordered list of filenames
    list = listdir(directory)
    for ignoredFile in ignoredFiles:
        if ignoredFile in list: list.remove(ignoredFile)
    list.sort(key=smartnumbers)
    return list

def pixelsAreEqual(im1,im2): # compares two images to see if there is duplicate information (overlap)
    return ImageChops.difference(im1, im2).getbbox() is None

myFileNames = list_screenshots(path)

firstImage = Image.open(path + '/' + myFileNames[0])
(width, height) = firstImage.size

compositeImage = Image.new("RGB", (width, len(myFileNames) * height), "red")

pixelsDown = 0

for fileName in myFileNames:
    screenshotImage = Image.open(path + '/' + fileName)
    if pixelsDown > 0:
        screenshotImage = screenshotImage.crop((0, iOSHeader, width, height))


        found = False
        overlap = 0
        topstrip = screenshotImage.crop((0, 0, width, overlapStripSize))
        while found == False and height > overlap:
            bottomstrip = compositeImage.crop((0, pixelsDown - overlapStripSize - overlap , width, pixelsDown - overlap))

            if pixelsAreEqual(topstrip, bottomstrip):
                found = True
                overlap = overlap + overlapStripSize
            else: overlap = overlap + 1

        if found:
            pixelsDown = pixelsDown - overlap
        compositeImage.paste(screenshotImage, (0, pixelsDown))
        pixelsDown = pixelsDown + height - iOSHeader
    else:
        compositeImage.paste(screenshotImage, (0, 0))
        pixelsDown = height

compositeImage = compositeImage.crop((0, 0, width, pixelsDown))
compositeImage.save(path + '/' + "composite.PNG", "PNG")
