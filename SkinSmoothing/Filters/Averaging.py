import cv2
import numpy as np

img = cv2.imread('D:/OpenCV/image/troy.jpg')

dst = cv2.blur(img, (5,5))

cv2.imshow('Original', img)
cv2.imshow('Averaging', dst)

cv2.imwrite("Averaging.jpg", dst)

cv2.waitKey(0)
cv2.destroyAllWindows()