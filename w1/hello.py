import cv2

img = cv2.imread("milady.jpg", 0)
def viewImage(img, name_of_window):
    cv2.namedWindow(name_of_window, cv2.WINDOW_GUI_NORMAL)
    cv2.imshow(name_of_window, img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()    
viewImage(img, "aa")