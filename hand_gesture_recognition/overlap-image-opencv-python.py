import cv2
import numpy as  np
img1 =cv2.imread("ex.png")#reads first image
img2 =cv2.imread("ex2.png")#reads seconds image
img3 =cv2.addWeighted(img1,.5,img2,.5,0)# intensity of both 1st and 2nd image is equal
cv2.imshow("abc",img1)#shows 1st image
cv2.imshow("abc2",img2)#shows 2nd image 
cv2.imshow("abc3",img3)#shows overlaped image
cv2.imwrite("over.jpg",img3)#saves overlaped image
cv2.waitKey()
cv2.destroyAllWindows()
