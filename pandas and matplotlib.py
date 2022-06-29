#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')
sns.set(color_codes=True)


# In[3]:


data1=pd.read_csv('D:\hemanth\da\gapminder_full.csv')


# In[4]:


#display dataset
data1


# In[5]:


#display the head of dataset(shows only 5 rows)
data1.head


# In[6]:


#get number of rows and columns
print(data1.shape
     )


# In[7]:


#get column names
data1.columns


# In[8]:


#get the dtype of each column
data1.dtypes


# In[9]:


#get more information about data
data1.info()


# In[10]:


#looking at columns,rows and cells
#get the country column and save it in a new variable 
country_data=data1['country']
#show first 5 observation
country_data.head()


# In[11]:


#get more information about data
data1.info()


# In[12]:


#show the last 5 observation
country_data.tail()


# In[13]:


#looking at country,continent and year
subset=data1[['country','continent','year']]
subset.head()


# In[14]:


#looking at country,continent,year
subset=data1[['country','continent','year']]
subset.head()


# In[15]:


subset.tail()


# In[16]:


#analytical summary of data set
data1.describe(include='all')


# In[17]:


#histogram of all the variables in the dataset
data1.hist(figsize=(10,5))


# In[20]:


#releationship between catagorical and continuousvariable
sns.boxplot(x="year",y="life_exp",data=data1)


# In[21]:


#drop irrrelavant columns
data1=data1.drop(['year'],axis="columns")
data1.head(5)


# In[23]:


#remaining the column name 
data1=data1.rename(columns={"country":"countries"})
data1.head(5)


# In[24]:


#rows containing dupliccate data
duplicate_rows=data1[data1.duplicated()]
print('number of duplicate rows:',duplicate_rows.shape)


# In[25]:


#count the rows before moving the data
data1.count()


# In[ ]:




