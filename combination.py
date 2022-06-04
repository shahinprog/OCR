
import cv2
import numpy as np

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


templates = []
templ_shapes = []
templ_name=["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"] 
similarity=[]
keypoints=[]
Templiste=[]
sorted=[]
faktor=10

for i in range(26):
    templates.append(cv2.imread('C:/Users/trpun/Desktop/OCR/Templates/New folder2/template{}.png'.format(i),0)) 
    templ_shapes.append(templates[i].shape[:: -1])


original = cv2.imread('C:/Users/trpun/Desktop/OCR/Photos/Untitled7.png')

ho,wo, _ = original.shape #h ,w
ho2=faktor*ho
wo2=faktor*wo
image=cv2.resize(original,(wo2,ho2))

gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
(thresh, im_bw) = cv2.threshold(gray, 128, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)


blur = cv2.GaussianBlur(im_bw, (7,7), 0)
thresh = cv2.threshold(blur, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)[1]
kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (5,5)) 
dilate = cv2.dilate(thresh, kernel, iterations=2)
cnts = cv2.findContours(dilate, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
cnts = cnts[0] if len(cnts) == 2 else cnts[1]

    
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

hey=[]

                   
def matching(cropped_image,x,y):#x , y are starting coordinates of cropped photo in original photo
         threshold = 1
         limit=0.1
         j=0  

         while threshold>limit:


               index=0
               #print("threshold")
               for template,templ_shape in zip(templates,templ_shapes):
           
                   
                   
                   hc,wc, _ = cropped_imagee.shape #h ,w

                   wc2=wc-2
                   hc2=hc-2
                   out=cv2.resize(template,(wc2,hc2))
           
                   res = cv2.matchTemplate(cropped_image, out, cv2.TM_CCOEFF_NORMED) 
                   #res = cv2.matchTemplate(cropped_image, template, cv2.TM_CCOEFF_NORMED)
                   loc = np.where( res >= threshold)
                   #print (loc) 
                   for pt in zip(*loc[::-1]):
                        hey.append((pt[0],pt[1]))
                   
                   if len(hey)>0:
                      last=threshold-0.1
                      #print(hey)
                      similarity.append((index,threshold,hey[0],(wc2,hc2)))

                      if last<=limit and len(templates)==index+1 :
                         similarity.sort(key=lambda x: x[1],reverse=True)
                         wt, ht = takeForth(similarity[j])
                         wr,hr=takeThird(similarity[j])
                         #cv2.rectangle(image, (wr+x, hr+y), (wt+x+wr, hr+ht+y), (255, 0, 0), 3)

                         
                             
                   hey.clear()    

                   index=index+1
        

   

               threshold=threshold-0.1 
         if len(similarity)>0:      
            return templ_name[takeFirst(similarity[j])] 

while n<len(sorted):
     x,y,w,h = sorted[n] 
     cropped_imagee = image[y:y+h, x:x+w] #crop_img = img[y:y+h, x:x+w]

     #cv2.imwrite('C:/Users/trpun/Desktop/OCR/Templates/New folder2/template{}.png'.format(n), cropped_imagee)



     gray2 = cv2.cvtColor(cropped_imagee, cv2.COLOR_BGR2GRAY)
     (thresh, im_bw2) = cv2.threshold(gray2, 128, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)
     
     	
     
    
     
     text=matching(im_bw2,x,y)# always inside gray
     #print(similarity)
     
     #print (text)
     #print("---------------")
     similarity.clear()
    
     relatvie_x=int(x/faktor)
     relative_y=int(y/faktor)
     relatvie_w=int(w/faktor)
     relatvie_h=int(h/faktor)
     original = cv2.rectangle(original, (relatvie_x, relative_y), (relatvie_x+ relatvie_w, relative_y + relatvie_h), (36,255,12), 1)

     cv2.putText(original, text, (relatvie_x, relative_y-10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (36,255,12), 2)
     n=n+1  
     

cv2.imshow('cropped_imagzzzzee',original)
#cv2.imshow('out',out) 
#cv2.imshow('im_gray',gray) 
cv2.waitKey(0)
