import cv2 as cv
import matplotlib.pylab as plt
from numpy import divide, int8, multiply, ravel, sort, zeros_like

def median_filter(gray_img, mask=3):
    # set image borders
    bd = int(mask / 2)
    # copy image size
    median_img = zeros_like(gray_img)
    for i in range(bd, gray_img.shape[0] - bd):
        for j in range(bd, gray_img.shape[1] - bd):
            # get mask according with mask
            kernel = ravel(gray_img[i - bd : i + bd + 1, j - bd : j + bd + 1])
            # calculate mask median
            median = sort(kernel)[int8(divide((multiply(mask, mask)), 2) + 1)]
            median_img[i, j] = median
    return median_img

plt.subplot(121)
image = cv.imread("Image_Kuis.jpg",cv.COLOR_BGR2GRAY)
plt.imshow(image)
filter=median_filter(image,3)
plt.subplot(122)
plt.imshow(filter)
plt.show()