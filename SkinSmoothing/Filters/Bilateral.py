import cv2
import numpy as np

img = cv2.imread('D:/OpenCV/image/troy.jpg')

dst = cv2.bilateralFilter(img, 9, 75, 75)

cv2.imshow('Original', img)
cv2.imshow('Bilateral', dst)

cv2.imwrite("Bilateral.jpg", dst)

cv2.waitKey(0)
cv2.destroyAllWindows()