import cv2
import numpy as np

img=cv2.imread("C:\\Users\\micah\\OneDrive - Asia Pacific University\\APU Materials\\Year 2 Semester 2\\Imaging & Special Effects\\Lab Activities\\Week 1\\stars.jpg")
image=cv2.imread("C:\\Users\\micah\\OneDrive - Asia Pacific University\\APU Materials\\Year 2 Semester 2\\Imaging & Special Effects\\Lab Activities\\Week 1\\stars.jpg")
img_c = cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
mask=np.zeros((img.shape[0],img.shape[1]))

for i in range(img_c.shape[0]):
    for j in range(img_c.shape[1]):
        if not (((img_c[i,j,0]>=90 and img_c[i,j,0]<=115) and img_c[i,j,1]>=20) and img_c[i,j,2]>=230): #to detect blue stars
            mask[i,j]=255
            img[i,j,:]=0

cv2.imshow("Color Detection",img)
cv2.imshow("Original Image",image)
cv2.imshow("HSV Image",img_c)
cv2.imshow("Mask",mask)
cv2.waitKey(0)