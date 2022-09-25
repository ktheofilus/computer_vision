import cv2 as cv
import matplotlib.pyplot as plt

src = (
10,10,70,65,10,
15,70,75,100,100,
15,70,100,100,100,
10,15,100,70,65,
15,15,10,70,10
)

print(src)

# eq=cv.equalizeHist(src)

plt.subplot(121), plt.hist(src),
plt.title("ori histogram") 

# plt.subplot(122), plt.hist(eq),
# plt.title("equalized histogram") 
# plt.xticks([]), plt.yticks([])

plt.show()

