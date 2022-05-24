import cv2
import numpy as np
threshold = 0.9

templates = []
templ_shapes = []

for i in range(2):
    templates.append(cv2.imread('C:/Users/trpun/Desktop/Project OCR/Templates/template{}.png'.format(i),0)) 
    templ_shapes.append(templates[i].shape[:: -1])

im_gray = cv2.imread('C:/Users/trpun/Desktop/crnn/Untitled2.png', cv2.IMREAD_GRAYSCALE)     
(thresh, im_bw) = cv2.threshold(im_gray, 128, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)

for template,templ_shape in zip(templates,templ_shapes): 
        res = cv2.matchTemplate(im_bw, template, cv2.TM_CCOEFF_NORMED) 
        loc = np.where( res >= threshold)
        w, h = templ_shape
        w1, h1= w, h
        for pt in zip(*loc[::-1]):
            cv2.rectangle(im_gray, pt, (pt[0] + w1, pt[1] + h1), (0,255,255), 2)    # Draw a rectangle around the matched region,#zip(loc[1],loc[0]) does the same as zip(*loc[:: -1])    
                                                                                            
cv2.imshow('im_gray',im_gray) 
cv2.imshow('template',template)
cv2.waitKey(0)
