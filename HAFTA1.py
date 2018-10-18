liste=[0,1,2,0,1,2,0,1,2,0,1,2,0,1,2,0,1,2,0,1]

for i in liste:
    print(int(i)+1)

for i in range(0,len(liste)):
    liste[i]=liste[i]+1

print(liste)

import random

s=random.randint(2,5)
print(s)

listee=[]
for i in range(10):
    listee.append(random.randint(0,10))
print(listee)

test_sayısı=100000

def createArray(s):
    myList=[]
    for i in range(s):
        myList.append(random.randint(0,10))
    return myList

def printArray(array):
    print(array)
    
def incArray(array):
    myList_1=[]
    for i in array:
        myList_1.append(i+1)
    return myList_1

def createArrayVersion(s):
    myList=np.arange(s)
    return myList

dizi_1=createArray(test_sayısı)
printArray(dizi_1)
dizi_2=incArray(dizi_1)
printArray(dizi_2)

import numpy as np
x=np.arange(10)
x

myL=createArrayVersion(test_sayısı)
myL=myL+25

myL[10025]

import matplotlib.pyplot as plt

image_1=plt.imread("test_1.jpg")

plt.imshow(image_1)
plt.show()

image_1.shape

type(image_1)