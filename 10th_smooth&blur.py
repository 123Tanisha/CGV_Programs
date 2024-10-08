import cv2
img=cv2.imread("Avatar.png")

gaussian_blur=cv2.GaussianBlur(img,(5,5),0)
median_blur=cv2.medianBlur(img,5)
bilateral_filter=cv2.bilateralFilter(img,9,75,75)

cv2.imshow('Original Image', img)
cv2.imshow('Gaussian Blur', gaussian_blur)
cv2.imshow('Median Blur', median_blur)
cv2.imshow('Bilateral Filter', bilateral_filter)

cv2.waitKey(0)
cv2.destroyAllWindows()
