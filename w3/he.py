import cv2 as cv
import matplotlib.pyplot as plt
import numpy as np

def showHist(image,color):
    plt.figure()

    for i,col in enumerate(color):
        histr = cv.calcHist([image],[i],None,[256],[0,256])
        plt.plot(histr,color = col)
        plt.xlim([0,256])

img = cv.imread("milady.jpg")
colors= ("red", "green", "blue")

showHist(img,colors)

plt.show()


