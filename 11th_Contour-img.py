import cv2
import numpy as np

img=cv2.imread("Avatar.png")
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

ret, thresh = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)
contours, hierarchy = cv2.findContours(thresh, cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
contour_img = img.copy()

cv2.drawContours(contour_img, contours, -1, (0, 255, 0), 2)

cv2.imshow('Original Img', img)
cv2.imshow('Contours', contour_img)

cv2.waitKey(0)
cv2.destroyAllWindows()
