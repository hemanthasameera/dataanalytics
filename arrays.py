#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
#create a 1d array
arr1=np.array([1,2,3])
print(arr1)


# In[2]:


#acessing  an element from an array

arr1[2]


# In[3]:


#change an element 
arr1[2]=5


# In[4]:


arr1


# In[5]:


#create a 2d array
arr2 = np.array([[1,2,3],[4,5,6]])
print(arr2)


# In[6]:


#check the shape of array
print("The shape is 2 rows and 3 columns",arr2.shape)


# In[7]:


#acessing the elements from the array
print(arr2[0][2])
print(arr2[0,2])
print(arr2[0,-1])
print(arr2[-1,0])


# In[8]:


# array of type string

arr3 = np.array(['India','china','usa','mexico'])
print(arr3)


# In[9]:


arr3[1]


# In[10]:


arr=np.arange(0,20,2)
print(arr)


# In[11]:


arr=np.linspace(0,20,2)
print(arr)


# In[12]:


arr=np.linspace(0,10,20)
print(arr)


# In[13]:


arr = np.random.rand(10)
print(arr)
arr = np.random.rand(3,4)
print(arr)


# In[14]:


# array of constant values in a given shape

print(np.full((4,6),10))


# In[15]:


#create an array by a repetition
#repeat each element of an array by a specified number of times

arr= [0,1,2]
print(np.repeat(arr,3))


# In[16]:


arr= [0,1,2]
print(np.tile(arr,3))


# In[17]:


identity_matrix = np.eye(3)
print(identity_matrix)


# In[20]:


arr = np.random.rand(5,5)
print(arr)


# In[21]:


identity_matrix = np.identity(3)
print(identity_matrix)


# In[22]:


#sum along the column

print(np.sum(arr,axis=0))


# In[23]:


#sum along the row

print(np.sum(arr,axis=0))


# In[24]:


print(np.mean(arr))
print(np.median(arr))
print(np.std(arr))
print(np.var(arr))


# In[25]:


#sort an array
arr=np.random.rand(5,5)
print(arr)


# In[26]:


#sorting along the row


print(np.sort(arr,axis=1))


# In[27]:


#append elements to an array
arr = np.array([4,5,6,7])


# In[28]:


arr1 = np.append(arr,8)
arr1


# In[29]:


arr2 = np.append(arr,[9,10,11])
print(arr2)


# In[30]:


#delete multiple elements
arr2 = np.array([4,5,6,7,9,10,11])
print(arr2)
print('\n')
arr5=np.delete(arr2,[1,4])
print(arr5)


# In[31]:


arr1=np.array([[1,2,3,4],[1,2,3,4]])
arr2=np.array([[5,6,7,8],[5,6,7,8]])


# In[32]:


cat = np.concatenate((arr1,arr2),axis=0)
print(cat)


# In[33]:


cat = np.concatenate((arr1,arr2),axis=1)
print(cat)


# In[ ]:




