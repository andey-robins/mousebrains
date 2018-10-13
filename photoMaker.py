import pygame
import math
import os
import time

def main():

    start = time.time()

    #clear all outImages
    for f in os.listdir("outImages/"):
        os.unlink("outImages/" + f)

    #object to store all files
    allFiles = []

    #find all files that have useable data
    for f in os.listdir("data/"):
        if 'fsl' in f:
            allFiles.append(f)

    #make images of all the files
    for f in allFiles:
        makePic(f)

    print('Process finished in: ' + str(time.time() - start) + ' seconds.')

    return

#pass the filename of a set of data and generate a screenshot of that data
def makePic(fileName):

    print('Making photo for file: ' + fileName)

    #exit for data that doesn't fit the model
    if "1020" in fileName:
        return

    dataValues = []
    size = 0

    fileName = fileName[:-4]

    #open and map all the values from a data file
    with open("data/" + fileName + ".txt", 'r') as f:
        for line in f:
            r, g, b = line.split()
            size += 1

            dataValues.append((map(r), map(g), map(b)))


    #make pygame to output the image
    pygame.init()
    screen = pygame.display.set_mode((24*16, 23*16))
    pygame.display.set_caption('Visualizer')

    #iterate through all the colors and draw the pictures
    index = 0
    for x in range(0, 24):
        for y in range(0, 23):
            pygame.draw.rect(screen, dataValues[index], (x*16, y*16, 16, 16))
            index += 1

    #generate the screenshot
    pygame.image.save(screen, "outImages/" + fileName + ".jpg")

    pygame.quit()

    return

#map the values from a data file to a 256 value for use as an RGB value
def map(num):
    return int(abs(math.floor(float(num)*255.0)))

if __name__ == '__main__':
    main()
