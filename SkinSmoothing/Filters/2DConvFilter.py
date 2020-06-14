import cv2
import numpy as np

img = cv2.imread('D:/OpenCV/image/troy.jpg')

kernel = np.ones((5,5), np.float32)/25
dst = cv2.filter2D(img, -1, kernel)

cv2.imshow('Original', img)
cv2.imshow('Conv2D', dst)

cv2.imwrite("Conv2D.jpg", dst)

cv2.waitKey(0)
cv2.destroyAllWindows()