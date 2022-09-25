import cv2
import matplotlib.pyplot as plt
import numpy as np


src=cv2.imread("milady.jpg")

scale_percent = 60 
width = int(src.shape[1] * scale_percent / 100)
height = int(src.shape[0] * scale_percent / 100)
dim = (width, height)
img = cv2.resize(src, dim, interpolation = cv2.INTER_AREA)

grayimg = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
eq = cv2.equalizeHist(grayimg)


plt.subplot(221), plt.imshow(grayimg), plt.title("original") 
plt.xticks([]), plt.yticks([])

plt.subplot(222), plt.imshow(cv2.cvtColor(eq, cv2.COLOR_BGR2RGB)),
plt.title("equalized") 
plt.xticks([]), plt.yticks([])

plt.subplot(223), plt.hist(grayimg),
plt.title("ori histogram") 
plt.xticks([]), plt.yticks([])

plt.subplot(224), plt.hist(eq),
plt.title("equalized histogram") 
plt.xticks([]), plt.yticks([])

plt.show()