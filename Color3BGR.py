import cv2
import numpy as np

img=cv2.imread("C:\\Users\\micah\\OneDrive - Asia Pacific University\\APU Materials\\Year 2 Semester 2\\Imaging & Special Effects\\Lab Activities\\Week 1\\flags.jpg")
image=cv2.imread("C:\\Users\\micah\\OneDrive - Asia Pacific University\\APU Materials\\Year 2 Semester 2\\Imaging & Special Effects\\Lab Activities\\Week 1\\flags.jpg")
mask=np.zeros((img.shape[0],img.shape[1]))

for i in range(img.shape[0]):
    for j in range(img.shape[1]):
        if not (img[i,j,0]>=100 and img[i,j,1]<=180 and img[i,j,2]<=120): #to detect blue in flags
            mask[i, j] = 255
            img[i,j,:]=0

cv2.imshow("Color Detection",img)
cv2.imshow("Original Image (BGR)",image)
cv2.imshow("Mask",mask)
cv2.waitKey(0)