import pygame
import math
# import os
#
# def main():
#
#     for f in
#
#     return

def makePic():

    dataValues = []
    size = 0

    fileName = 'datafile'

    with open(fileName + '.txt', 'r') as f:
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
    pygame.image.save(screen, fileName + '.jpg')

    pygame.quit()

    return

#map the values from a data file to a 256 value for use as an RGB value
def map(num):
    return int(abs(math.floor(float(num)*255.0)))

if __name__ == '__main__':
    main()
