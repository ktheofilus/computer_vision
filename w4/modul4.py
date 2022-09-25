import numpy as np
import cv2
import matplotlib.pyplot as plt

# load image dan ubah ke gray
img = cv2.imread("nacka.jpg")
gray_img=cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# inisialisasi filter gradient
horizontal = np.array([[0, 0, 0], [0, -1, 0], [0, 1, 0]]) # s2
vertical = np.array([[0, 0, 0], [0, -1, 1], [0, 0, 0]]) # s1

# inisialisasi tinggi/baris dan lebar/kolom image sebagai Batasan looping
h, w = gray_img.shape
newgradientImage = np.zeros([h, w]) #untuk membuat variable hasil dimana dimensinya sesuai
#dengan tinggi dan lebar image dan di beri nilai 0
#menghitung hasil image dikenai filter gradient, bisa juga dengan memanfaatkan library opencv
#➔ cv2.filter2D(img, -1, filterhorizontal/vertical)
for i in range(1, h - 1):
    for j in range(1, w - 1):

        horizontalGrad = (horizontal[0, 0] * gray_img[i - 1, j - 1]) + \
        (horizontal[0, 1] * gray_img[i - 1, j]) + \
        (horizontal[0, 2] * gray_img[i - 1, j + 1]) + \
        (horizontal[1, 0] * gray_img[i, j - 1]) + \
        (horizontal[1, 1] * gray_img[i, j]) + \
        (horizontal[1, 2] * gray_img[i, j + 1]) + \
        (horizontal[2, 0] * gray_img[i + 1, j - 1]) + \
        (horizontal[2, 1] * gray_img[i + 1, j]) + \
        (horizontal[2, 2] * gray_img[i + 1, j + 1])

        verticalGrad = (vertical[0, 0] * gray_img[i - 1, j - 1]) + \
        (vertical[0, 1] * gray_img[i - 1, j]) + \
        (vertical[0, 2] * gray_img[i - 1, j + 1]) + \
        (vertical[1, 0] * gray_img[i, j - 1]) + \
        (vertical[1, 1] * gray_img[i, j]) + \
        (vertical[1, 2] * gray_img[i, j + 1]) + \
        (vertical[2, 0] * gray_img[i + 1, j - 1]) + \
        (vertical[2, 1] * gray_img[i + 1, j]) + \
        (vertical[2, 2] * gray_img[i + 1, j + 1])

        # mendapatkan kekuatan tepi (edge magnitude)
        mag = np.sqrt(pow(horizontalGrad, 2.0) + pow(verticalGrad, 2.0))
        newgradientImage[i - 1, j - 1] = mag

#menampilkan hasil image gradient
plt.figure()
plt.title('gradient1.png')
plt.imsave('gradient1.png', newgradientImage, cmap='gray', format='png')
plt.imshow(newgradientImage, cmap='gray')
plt.show()