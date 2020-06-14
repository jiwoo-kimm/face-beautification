import cv2
import numpy as np

img = cv2.imread('D:/OpenCV/image/mika.jpg')

dst = cv2.ximgproc.guidedFilter(img, img, 5, 200)

cv2.imshow('Original', img)
cv2.imshow('Guided', dst)

cv2.imwrite("D:/OpenCV/image/filtered/mika_g.jpg", dst)

cv2.waitKey(0)
cv2.destroyAllWindows()