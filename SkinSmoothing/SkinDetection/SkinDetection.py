import cv2
import numpy as np


# Open an image
img = cv2.imread("D:/OpenCV/image/lee.jpg")

# HSV
img_HSV = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)  # Convert color space
HSV_mask = cv2.inRange(img_HSV, (0, 15, 0), (17, 170, 255))   # Set up range
HSV_mask = cv2.morphologyEx(HSV_mask, cv2.MORPH_OPEN, np.ones((3, 3), np.uint8))

# YCbCr
img_YCrCb = cv2.cvtColor(img, cv2.COLOR_BGR2YCrCb)  # Convert color space
YCrCb_mask = cv2.inRange(img_YCrCb, (0, 135, 85), (255, 180, 135))    # Set up range
YCrCb_mask = cv2.morphologyEx(YCrCb_mask, cv2.MORPH_OPEN, np.ones((3, 3), np.uint8))

# Merge skin detection (YCbCr + HSV)
global_mask = cv2.bitwise_and(YCrCb_mask, HSV_mask)
global_mask = cv2.medianBlur(global_mask, 3)
global_mask = cv2.morphologyEx(global_mask, cv2.MORPH_OPEN, np.ones((4, 4), np.uint8))

# Make results
HSV_result = cv2.bitwise_not(HSV_mask)
YCrCb_result = cv2.bitwise_not(YCrCb_mask)
global_result = cv2.bitwise_not(global_mask)

# Show results
cv2.imshow("1_troy.jpg", HSV_result)
cv2.imshow("2_troy.jpg", YCrCb_result)
cv2.imshow("3_troy.jpg", global_result)

# Save results
cv2.imwrite("1_HSV.jpg", HSV_result)
cv2.imwrite("2_YCbCr.jpg", YCrCb_result)
cv2.imwrite("3_global_result.jpg", global_result)

cv2.waitKey(0)
cv2.destroyAllWindows()