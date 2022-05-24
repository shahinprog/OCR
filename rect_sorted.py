
import cv2
import numpy as np



image = cv2.imread('C:/Users/trpun/Desktop/Project OCR/Photos/Untitled2.png')
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
blur = cv2.GaussianBlur(gray, (7,7), 0)
thresh = cv2.threshold(blur, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)[1]
kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (5,5)) 
dilate = cv2.dilate(thresh, kernel, iterations=2)
cnts = cv2.findContours(dilate, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
cnts = cnts[0] if len(cnts) == 2 else cnts[1]
keypoints=[]
Templiste=[]
sorted=[]
def takeFirst(elem): # takes list as an argument takeFirst(keypoints[0])
    return elem[0]
def takeSecond(elem):
    return elem[1]    
def takeThird(elem):
    return elem[2]
def takeForth(elem):
    return elem[3]
def remove_items_from_list(keypoints, Templiste):
        n = len(keypoints)
        for i in range(n - 1, -1, -1):
            if keypoints[i] in Templiste:
               del keypoints[i]      
all_elements=0
b=0       
for c in cnts:
    all_elements=all_elements+1       

    x,y,w,h = cv2.boundingRect(c)
    keypoints.append( (x,y,w,h) )
while b < len(keypoints):             
    keypoints.sort(key=lambda x: x[0]+x[1])
    z=takeSecond(keypoints[0])+takeForth(keypoints[0])/2
    index=0
    while index < len(keypoints): 

        if((takeSecond(keypoints[index])+takeForth(keypoints[index]))>=z and takeSecond(keypoints[index])<=z):
           Templiste.append( (takeFirst(keypoints[index]),takeSecond(keypoints[index]),takeThird(keypoints[index]),takeForth(keypoints[index])) )
        index=index+1     
    Templiste.sort(key=lambda x: x[0])
    counterrr=0
    for i in Templiste:
        sorted.append(Templiste[counterrr])
        counterrr=counterrr+1

    remove_items_from_list(keypoints, Templiste)
    
    Templiste.clear()
n=0                    
while n<len(sorted):
     x,y,w,h = sorted[n]
     text=str(n)
     image = cv2.rectangle(image, (x, y), (x + w, y + h), (36,255,12), 1)
     cv2.putText(image, text, (x, y-10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (36,255,12), 2)
     n=n+1  

#print(len(sorted))


cv2.imshow('image', image)
cv2.waitKey()    
