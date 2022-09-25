import cv2 as cv
import numpy as np
import matplotlib.pyplot as pl
img = cv.imread('milady.jpg')
b, g, r = cv.split(img) #memisah citra perkanal
fig, ax = pl.subplots(1, 3, figsize=(16, 8))
pl.subplot(231)
pl.imshow(img[...,::-1]) #citra asli
pl.title('Citra Warna')
pl.subplot(232)
pl.imshow(cv.cvtColor(b, cv.COLOR_BGR2RGB)) #karena ditampilkan dari matplotlib maka
#harus diconvert ke RGB dari citra BGR
pl.title('Citra Warna Channel B')
pl.subplot(233)
pl.imshow(cv.cvtColor(g, cv.COLOR_BGR2RGB))
pl.title('Citra Warna Channel G')
pl.subplot(234)
pl.imshow(cv.cvtColor(r, cv.COLOR_BGR2RGB))
pl.title('Citra Warna Channel R')

pl.subplot(235)
pl.imshow(cv.merge((r,g,b)))
pl.title('Citra Warna Channel RGB')
pl.show()
