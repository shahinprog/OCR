
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
templ_name=["A","a","B","b","C","c","D","d","E","e","F","f","G","g","H","h","I","i","J","j","K","k","L","l","M","m","N","n","o","P","p","Q","q","R","r","S","s","T","t","U","u","V","v","W","w","X","x","Y","y","z"]
similarity=[]
keypoints=[]
Templiste=[]
sorted=[]
faktor=10

for i in range(49):
    templates.append(cv2.imread('C:/Users/trpun/Desktop/OCR/Templates/New folder/template{}.png'.format(i),0)) 
    templ_shapes.append(templates[i].shape[:: -1])


original = cv2.imread('C:/Users/trpun/Desktop/OCR/Photos/Untitled14.png')

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
    keypoints.sort(key=lambda x: x[0]+x[1])#x+y
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

temp=[]
 
# Function to convert  
def listToString(s): 
    
    # initialize an empty string
    str1 = "" 
    
    # return string  
    return (str1.join(s))
        
        
  
                  
def matching(cropped_image,x,y):#x , y are starting coordinates of cropped photo in original photo
         threshold = 1
         limit=0.1
         j=0  

         while threshold>limit:


               index=0
               #print("threshold")
               for template in templates:
           
                   
                   
                   hc,wc, _ = cropped_imagee.shape #h ,w

                   wc2=wc-2
                   hc2=hc-2
                   out=cv2.resize(template,(wc2,hc2))
           
                   res = cv2.matchTemplate(cropped_image, out, cv2.TM_CCOEFF_NORMED) 
                   #res = cv2.matchTemplate(cropped_image, template, cv2.TM_CCOEFF_NORMED)
                   loc = np.where( res >= threshold)
                   #print (loc) 
                   for pt in zip(*loc[::-1]):
                        temp.append((pt[0],pt[1]))
                   
                   if len(temp)>0:
                      last=threshold-0.1
                      #print(temp)
                      similarity.append((index,threshold,temp[0],(wc2,hc2)))

                      if last<=limit and len(templates)==index+1 :
                         similarity.sort(key=lambda x: x[1],reverse=True)
                         wt, ht = takeForth(similarity[j])
                         wr,hr=takeThird(similarity[j])
                         #cv2.rectangle(image, (wr+x, hr+y), (wt+x+wr, hr+ht+y), (255, 0, 0), 3)

                         
                             
                   temp.clear()    

                   index=index+1
        

   

               threshold=threshold-0.1 
         if len(similarity)>0:      
            return templ_name[takeFirst(similarity[j])] 
newlist=[]
newlist = sorted.copy()
newlist.sort(key=lambda x: x[3],reverse=True)
#print(newlist)
max_h=takeForth(newlist[0]) 


words=[]
words_temp=[]


average_dist=int(max_h/4) 
print(average_dist)
        

while n<len(sorted):

     x,y,w,h = sorted[n] 
     if n+1<len(sorted):
        x2,y2,w2,h2 = sorted[n+1]

     cropped_imagee = image[y:y+h, x:x+w] #crop_img = img[y:y+h, x:x+w]

     gray2 = cv2.cvtColor(cropped_imagee, cv2.COLOR_BGR2GRAY)
     (thresh, im_bw2) = cv2.threshold(gray2, 128, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)

     
     text=matching(im_bw2,x,y)# always inside gray

     rect_dist=x2-x-w

    
     if rect_dist<average_dist:
        words_temp.append(text)
     else:
         if len(words_temp)>0:
             words_temp.append(text)
             word=listToString(words_temp)

             words.append(word)
             #print("words temp is   ",words_temp)
             #print("---------------") 
             #print("words is   ",words)
             #print("---------------")  
          
             words_temp.clear()

     similarity.clear()
    
     relatvie_x=int(x/faktor)
     relative_y=int(y/faktor)
     relatvie_w=int(w/faktor)
     relatvie_h=int(h/faktor)
     original = cv2.rectangle(original, (relatvie_x, relative_y), (relatvie_x+ relatvie_w, relative_y + relatvie_h), (36,255,12), 1)

     cv2.putText(original, text, (relatvie_x, relative_y-10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (36,255,12), 2)
     n=n+1
      
   
     
print(words)
#cv2.imshow('cropped_imagzzzzee',original)
cv2.waitKey(0)
