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
if 0 == len(myFileNames): raise Exception('there aren\'t any images in your images folder, dingus')

firstImage = Image.open(path + '/' + myFileNames[0])
(width, height) = firstImage.size

compositeImage = Image.new("RGB", (width, len(myFileNames) * height), "red")

pixelsDown = 0

for fileName in myFileNames:
    screenshotImage = Image.open(path + '/' + fileName) # opens the current image file, creates a new object out of it and calls it screenshotImage

    if 0 == pixelsDown: # pastes the first image in the series to the top of our canvas
        compositeImage.paste(screenshotImage, (0, 0))
        pixelsDown = height
        continue

    screenshotImage = screenshotImage.crop((0, iOSHeader, width, height)) # crops the header off the succeding screenshots

    foundMatchingStrip = False
    overlap = 0
    topstrip = screenshotImage.crop((0, 0, width, overlapStripSize))
    while not foundMatchingStrip and overlap < height:
        bottomstrip = compositeImage.crop((0, pixelsDown - overlapStripSize - overlap , width, pixelsDown - overlap))

        if not pixelsAreEqual(topstrip, bottomstrip):
          overlap = overlap + 1
        else:
            foundMatchingStrip = True
            overlap = overlap + overlapStripSize

    if foundMatchingStrip:
        pixelsDown = pixelsDown - overlap
    compositeImage.paste(screenshotImage, (0, pixelsDown))
    pixelsDown = pixelsDown + height - iOSHeader

compositeImage = compositeImage.crop((0, 0, width, pixelsDown)) # crops the canvas to the correct size now that all screenshots have been placed and cropped appropriately
compositeImage.save(path + '/' + "composite.PNG", "PNG")