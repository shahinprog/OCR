
from combination import words
from itertools import zip_longest

# opening the file in read mode
my_file = open("words_20k.txt", "r")
  
# reading the file
data = my_file.read()
  
# replacing end splitting the text 
# when newline ('\n') is seen.
words_dict = data.split("\n")

my_file.close()



#print(content_list[100])
def takeFirst(elem): # takes list as an argument takeFirst(keypoints[0])
    return elem[0]
def takeSecond(elem):
    return elem[1]    
def takeThird(elem):
    return elem[2]
def takeForth(elem):
    return elem[3]




def hamming_distance(s1, s2):
    return  sum(c1 != c2 for c1, c2 in zip_longest(s1, s2))


  
Temp_correct=[]
correct=[]


n=0
while n<len(words):
      z=0

      while z<len(words_dict):

          str1 = words[n]
          str2 = words_dict[z]
          
          temp_hamming_distance=hamming_distance(str1,str2)
          Temp_correct.append((temp_hamming_distance,str2))


          z=z+1

      Temp_correct.sort(key=lambda x: x[0])
      correct.append (takeSecond(Temp_correct[0])) 
      #print(takeFirst(Temp_correct[10]))
      Temp_correct.clear()

      n=n+1

print("words are ",words)
print("correct are ",correct)