import cv2
import numpy as np

img = cv2.imread('D:/OpenCV/image/troy.jpg')

dst = cv2.GaussianBlur(img, (5,5), 0)

cv2.imshow('Original', img)
cv2.imshow('Gaussian', dst)

cv2.imwrite("Gaussian.jpg", dst)

cv2.waitKey(0)
cv2.destroyAllWindows()