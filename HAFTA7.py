
# coding: utf-8

# In[27]:
#a) 28x28 boyutlarında içeriği 0 ve 1 olan bir matris üretiniz.
#b) a'da üretilen matriste 1'leri içeren MBR dikdörtgeni üreten fonksiyonu yazınız.
#c) Kendisine aktarılan(gönderilen) iki vektörün benzerliğini return eden fonksiyonu yazınız.
#d)a şıkkında yazılan fonksiyonu kullanarak 100 farklı matris elde edip 1. üretilen ile diğerlerini karşılaştırıp yakınlığını ve benzerliğini listeleyiniz.

import random
import numpy as np
def matris_create_28_by_28_with_0_1():                          #a şıkkı
        my_matris=np.zeros((28,28))
        for i in range(28):
            for j in range(28):
                my_matris[i,j]=random.randint(0,1)
        return my_matris
def MBR_create_28_by_28_with_0_1(matris_a):                      #b şıkkı
        m=matris_a.shape[0]
        n=matris_a.shape[1]
        x_min=m
        x_max=0   #baslangıç değerleri olası en olumsuz durum
        y_min=n
        y_max=0
        for i in range(m):
            for j in range(n):
                if (matris_a[i,j]==1 and x_min>i):   #resim/matris üzerinden
                    x_min=i                         #x_min,....... güncelleniyor
                if (matris_a[i,j]==1 and x_max<i):
                    x_max=i
                if (matris_a[i,j]==1 and y_min>j):
                    y_min=i
                if (matris_a[i,j]==1 and y_max<j):
                    y_max=i
        return (x_min, x_max, y_min, y_max)
    
def get_similarity(character_a,character_b):                       #c şıkkı
    m=character_a.shape[0]
    n=character_a.shape[1]
    my_similarity=0
    for i in range(m):
        for j in range(n):
            my_similarity=my_similarity+character_a[i,j]*character_b[i,j]
    return my_similarity



# In[28]:

def get_similarity_for_100_character(kac_karakter=100):             #d şıkkı
    characters=[]  
    for i in range(kac_karakter):
        new_char=matris_create_28_by_28_with_0_1()
        characters.append(new_char)
    for j in range(kac_karakter):
        benzerlik=get_similarity(characters[0],characters[i])
        print(" 0 --"+str(i)+" ", benzerlik)


# In[29]:

c_1= matris_create_28_by_28_with_0_1()   #m, MBR_create_28_by_28_with_0_1(m)
c_2= matris_create_28_by_28_with_0_1()
get_similarity(c_1,c_2)
get_similarity_for_100_character(10)


# In[30]:

m=matris_create_28_by_28_with_0_1()
MBR_create_28_by_28_with_0_1(m)


# In[ ]:



