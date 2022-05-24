import cv2
import numpy as np




im_gray = cv2.imread('C:/Users/trpun/Desktop/Project OCR/Photos/Untitled2.png', cv2.IMREAD_GRAYSCALE)
(thresh, im_bw) = cv2.threshold(im_gray, 128, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)



template = cv2.imread("C:/Users/trpun/Desktop/Project OCR/Templates/template0.png", cv2.IMREAD_GRAYSCALE) 
(thresh, im_bw2) = cv2.threshold(template, 128, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)  

w, h = template.shape[::-1]

res = cv2.matchTemplate(im_bw,template,cv2.TM_CCOEFF_NORMED)

threshold = 0.9

loc = np.where( res >= threshold)
print (loc)

for pt in zip(*loc[::-1]):
	cv2.rectangle(im_gray, pt, (pt[0] + w, pt[1] + h), (0,255,255), 2)

cv2.imshow('Detected',im_gray) 
cv2.imshow('Detectedd',im_bw2)


cv2.waitKey(0)





