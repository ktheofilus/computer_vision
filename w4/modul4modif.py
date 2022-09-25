import numpy as np
import cv2 as cv
import matplotlib.pyplot as plt

def convolution(img,xfilter,yfilter):
    #empty image
    temp_img = np.zeros_like(gray_img)

    #get height,width
    h, w = img.shape

    #convolution process
    for i in range(1, h - 1):
        for j in range(1, w - 1):
            horizontalGrad = + \
                (xfilter[0, 0] * gray_img[i - 1, j - 1]) + \
                (xfilter[0, 1] * gray_img[i - 1, j]) + \
                (xfilter[0, 2] * gray_img[i - 1, j + 1]) + \
                (xfilter[1, 0] * gray_img[i, j - 1]) + \
                (xfilter[1, 1] * gray_img[i, j]) + \
                (xfilter[1, 2] * gray_img[i, j + 1]) + \
                (xfilter[2, 0] * gray_img[i + 1, j - 1]) + \
                (xfilter[2, 1] * gray_img[i + 1, j]) + \
                (xfilter[2, 2] * gray_img[i + 1, j + 1])
            verticalGrad = +\
                (yfilter[0, 0] * gray_img[i - 1, j - 1]) + \
                (yfilter[0, 1] * gray_img[i - 1, j]) + \
                (yfilter[0, 2] * gray_img[i - 1, j + 1]) + \
                (yfilter[1, 0] * gray_img[i, j - 1]) + \
                (yfilter[1, 1] * gray_img[i, j]) + \
                (yfilter[1, 2] * gray_img[i, j + 1]) + \
                (yfilter[2, 0] * gray_img[i + 1, j - 1]) + \
                (yfilter[2, 1] * gray_img[i + 1, j]) + \
                (yfilter[2, 2] * gray_img[i + 1, j + 1])
                
            edge = np.sqrt(pow(horizontalGrad, 2.0) + pow(verticalGrad, 2.0))
            temp_img[i, j] = edge
    print("convolution done!")
    return temp_img

def rescale(img,scale_percent):
    width = int(img.shape[1] * scale_percent / 100)
    height = int(img.shape[0] * scale_percent / 100)
    dim = (width, height)
    return cv.resize(img, dim, interpolation = cv.INTER_AREA)
  
#load
src = plt.imread("nacka.jpg")

#rescale
img = rescale(src,100)
gray_img=cv.cvtColor(img, cv.COLOR_RGB2GRAY)

#show image
plt.subplot(221)
plt.title("gray_img")
plt.imshow(gray_img)

#filter gradient
xGradFilter = np.array([
    [0, 0, 0], 
    [0, -1, 0], 
    [0, 1, 0]
])
yGradFilter = np.array([
    [0, 0, 0], 
    [0, -1, 1], 
    [0, 0, 0]
])
plt.subplot(222)
plt.title("gradient_filter")
gradImg=convolution(gray_img,xGradFilter,yGradFilter)
plt.imshow(gradImg)

#filter laplace
xLaplaceFilter = np.array([
    [0, 1, 0], 
    [1, -4, 1], 
    [0, 1, 0]
])
yLaplaceFilter = np.array([
     [0, 1, 0], 
    [1, -4, 1], 
    [0, 1, 0]
])
plt.subplot(223)
plt.title("laplace_filter")
lapImg=convolution(gray_img,xLaplaceFilter,yLaplaceFilter)
plt.imshow(lapImg)

#filter gradient+laplace
plt.subplot(224)
plt.title("gradient_laplace_filter")
gradLapImg=convolution(gradImg,xLaplaceFilter,yLaplaceFilter)
plt.imshow(gradLapImg)

plt.show()
