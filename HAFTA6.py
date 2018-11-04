
# coding: utf-8

# In[44]:

import numpy as np
import matplotlib.pyplot as plt
img=plt.imread("resim.jpg")
plt.subplot(1,2,2)
plt.imshow(img,cmap='Greys',interpolation='nearest')
plt.show()


# In[45]:

internal_mask_1=[[1,0],[0,0]]
internal_mask_2=[[0,1],[0,0]]
internal_mask_3=[[0,0],[1,0]]
internal_mask_4=[[0,0],[0,1]]

external_mask_1=[[0,1],[1,1]]
external_mask_2=[[1,0],[1,1]]
external_mask_3=[[1,1],[0,1]]
external_mask_4=[[1,1],[1,0]]

internal_mask_list=[internal_mask_1,internal_mask_2,internal_mask_3,internal_mask_4]
external_mask_list=[external_mask_1,external_mask_2,external_mask_3,external_mask_4]


# In[54]:

def get_distance(v, w= [1/3, 1/3, 1/3]):
    a,b,c = v[0],v[1],v[2]
    w1,w2,w3 = w[0],w[1],w[2]
    d = ((a**2)*w1+(b**2)*w2+(c**2)*w3)**.5
    return d


def convert_rgb_to_gray_level(im_1):
    m = im_1.shape[0]
    n = im_1.shape[1]
    im_2 = np.zeros((m,n))
    for i in range (m):
        for j in range(n):
            im_2[i,j] = get_distance(im_1[i,j,:])
    return im_2


# In[47]:


def convert_gray_level_to_bw(image_gray_level):
    m = image_gray_level.shape[0]
    n = image_gray_level.shape[1]
    im_bw = np.zeros((m,n))
    for i in range(m):
        for j in range(n):
            if image_gray_level[i,j]>120:
                im_bw[i,j] = 1
            else:
                im_bw[i,j] = 0
    return im_bw


# In[55]:

convert_rgb_to_gray_level(img)
convert_gray_level_to_bw(img)


# In[56]:

def count(image,mask):
    counter=0
    m=image.shape[0]
    n=image.shape[1]
    for i in range(1,m-1):
        for j in range(1,n-2):
            x=y=z=d=False
            if(image[i,j] == mask[0][0]):
                x=True
            if(image[i,j+1] == mask[0][1]):
                y=True
            if(image[i+1,j] == mask[1][0]):
                z=True
            if(image[i+1,j+1] == mask[1][1]):
                d=True
            if(x and y and z and d):
                counter=counter+1
    return counter            


# In[36]:

count(img,internal_mask_list)


# In[39]:

def count_internal_mask(image):
    counter_internal=0
    for mask in internal_mask_list:
        counter_internal=counter_internal+count(img_1,mask)
    return counter_internal
    
def count_external_mask(image):
    counter_external=0
    for mask in external_mask_list:
        counter_external=counter_external+count(img_1,mask)
    return counter_external


# In[43]:

my_block=img[10:12,50:52]
my_block=my_block.reshape(1,4)
my_block.shape
s=0
for i in range(4):
    if(my_block[0,i]==1): # 1 internal iç köşe, 0 dış köşe
        s=s+2**i
if s==8 or s==4 or s==2 or s==1:
    return True ## e=e+1
else:
    return False

