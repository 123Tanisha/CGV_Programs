import cv2
import numpy as np

img_path="Avatar.png"
img=cv2.imread(img_path)
height,width,_=img.shape

rotation_matrix=cv2.getRotationMatrix2D((width/2, height/2), 45, 1) 
scaling_matrix = np.float32([[1.5, 0, 0], [0, 1.5, 0]]) 
translation_matrix = np.float32([[1, 0, 100], [0, 1, 50]]) 

rotated_img = cv2.warpAffine(img, rotation_matrix, (width, height))
scaled_img = cv2.warpAffine(img, scaling_matrix, (int(width*1.5), int(height*1.5)))
translated_img = cv2.warpAffine(img, translation_matrix, (width, height))

cv2.imshow("Original Image", img)
cv2.imshow("Rotated Image", rotated_img)
cv2.imshow("Scaled Image", scaled_img)
cv2.imshow("translated Image", translated_img)

cv2.waitKey(0)
cv2.destroyAllWindows()