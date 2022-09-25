from re import M
import cv2
import matplotlib.pyplot as plt
import numpy as np
# img = cv2.imread("milady.jpg") #silahkan diganti dengan image lain bebas
# img1 = cv2.cvtColor(img, cv2.COLOR_BGR2RGB) #untuk meng-convert BGR ke RGB
img = plt.imread("milady.jpg")
plt.imshow(img)
plt.show()
print('Image Dimensions :', img.shape) #untuk melihat dimensi(ukuran) gbr dlm pixel
gray_img = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY) #untuk meng-convert RGB ke Gray
print(gray_img) #untuk menampilkan citra keabuan dalam bentuk array 2 Dimensi
