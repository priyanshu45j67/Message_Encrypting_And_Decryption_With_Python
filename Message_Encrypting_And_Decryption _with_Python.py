import string
import random
def random_char(y):
   return "".join(random.choice(string.ascii_letters)for x in range(y))

str=input("Enter the string\n")
list=str.split()
newlist=[]
coding=input("Press 1 for coding\n Press 2 for decoding\n")
coding=True if coding=="1" else False
if(coding):
 for words in list:

   if(len(words)>=3):
     r1=random_char(3)
     r2=random_char(3)
     strnew=r1+words[1:]+words[0]+r2
     newlist.append(strnew)
   else:
     newlist.append(words[::-1])
 print(" ".join(newlist))
else:
  for words in list:
    if(len(words)>=3):
      strnew=words[3:-3]
      strnew=strnew[-1]+strnew[:-1]
      newlist.append(strnew)
    else:
      newlist.append(words[::-1])
  print(" ".join(newlist))