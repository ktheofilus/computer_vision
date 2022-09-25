import cv2
import matplotlib.pyplot as plt
import numpy as np
img = cv2.imread("milady.jpg") #silahkan diganti dengan image lain bebas
img1 = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
gray_img = cv2.cvtColor(img1, cv2.COLOR_RGB2GRAY)
#menggunakan fungsi subplot(jumlahbaris,jumlahkolom,indeks-ke) dari matplotlib untuk menampilkan 2 gambar agar lebih rapi
plt.subplot(211), plt.imshow(img1), plt.title("Original") #image sudah RGB
plt.xticks([]), plt.yticks([]) #menghapus x dan y axis
plt.subplot(212), plt.imshow(cv2.cvtColor(gray_img, cv2.COLOR_BGR2RGB)),
plt.title("Edited") #dari BGR ke Gray
plt.xticks([]), plt.yticks([])
plt.show()