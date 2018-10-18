
# coding: utf-8

# In[19]:

#fonksiyon 3 değer alacak ve geriye distance gönderecek
def get_distance(v,w=[1/3,1/3,1/3]): #w ağırlık değeri
    a,b,c=v[0],v[1],v[2]
    w1,w2,w3=w[0],w[1],w[2]
    d= ((a**2)*w1+
    (b**2)*w2+
    (c**2)*w3)**.5
    #d=((a*w1)**2+(b*w2)**2+(c*w3)**2)**.5
    return d


# In[58]:

def convert_gray_level_to_BW(image_gray_level):
    m=image_gray_level.shape[0]
    n=image_gray_level.shape[1]
    im_bw=np.zeros((m,n)) #im2 boyutunu bilmediğimiz için bunu yazdık. bu bize iki boyutlu bir yapı oluşturur.
    for i in range(m):
        for j in range (n):
            if image_gray_level[i,j]>120:
                im_bw[i,j]=1
            else:
                im_bw[i,j]=0
            
    return im_bw


# In[50]:

def convert_rgb_to_gray_level(im_1):
    m=im_1.shape[0]
    n=im_1.shape[1]
    im_2=np.zeros((m,n)) #im2 boyutunu bilmediğimiz için bunu yazdık. bu bize iki boyutlu bir yapı oluşturur.
    for i in range(m):
        for j in range (n):
            im_2[i,j]=get_distance(im_1[i,j,:])
    return im_2


# In[63]:

import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import numpy as np
im_1=mpimg.imread('Tree.jpg')
im_2=convert_rgb_to_gray_level(img)
im_3=convert_gray_level_to_BW(im_2)
get_ipython().magic('matplotlib inline')
plt.imshow(img)plt.subplot(1,3,1),plt.imshow(im_1)
plt.subplot(1,3,2),plt.imshow(im_2,cmap='gray')
plt.subplot(1,3,3),plt.imshow(im_3,cmap='gray')


# In[20]:

my_RGB=[1,2,3]
gray_level=get_distance(my_RGB)
print(gray_level)


# In[21]:

my_RGB=[10,20,3]
gray_level=get_distance(my_RGB,[.6,.3,.1])
print(gray_level)


# In[43]:

im_2.max()


# In[57]:

import matplotlib.pyplot as plt
img=plt.imread("Tree.jpg")
av=plt.imshow(img)
plt.show()


# In[51]:

im_2=convert_rgb_to_gray_level(img)
type(im_2)


# In[34]:

img.shape, im_2.shape


# In[41]:

plt.imshow(im_2,cmap='gray')


# In[ ]:




# In[ ]:




# In[ ]:




# In[ ]:




# In[ ]:



