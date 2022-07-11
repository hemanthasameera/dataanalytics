#!/usr/bin/env python
# coding: utf-8

# In[2]:


import pandas as pd
import numpy as np


# In[3]:


#dataframe will have its index assigned automatically
#the columns are placed in "sorted order 
data={'state':['Ohio','Ohio','Ohio','Nevada','Nevada','Nevada'],'year':[2000,2001,2002,2001,2002,2003],
     'pop':[1.5,1.7,3.6,2.4,2.9,3.2]}
frame=pd.DataFrame(data)
#using the Jupyter notebook,pandas dataframe objects will be displayed as a more brwser-friendly HTML table.
frame


# In[4]:


frame.head()


# In[5]:


pd.DataFrame(data,columns=['year','state','pop'])


# In[6]:


frame2=pd.DataFrame(data, columns=['year','state','pop','debt'],index=['one','two','three','four','five','six'])
frame2


# In[7]:


frame2.columns


# In[8]:


frame2['state']


# In[9]:


frame2.year


# In[10]:


frame2.loc['three']


# In[12]:


frame2['debt']=16.5
frame2


# In[14]:


frame2['debt'] = np.arrange(6.)
frame2


# In[15]:


frame2['debt']=np.arange(6.)
frame2


# In[16]:


val=pd.Series([-1.2,-1.5,-1.7],index=['two','four','five'])
frame2['debt']=val
frame2


# In[17]:


frame2['eastern']=frame2.state=='Ohio'
frame2


# In[18]:


del frame2['eastern']
frame2.columns


# In[19]:


pop={'Nevada':{2001:2.4,2002:2.9},'Ohio':{2000:1.5,2002:1.7,2002:3.6}}
frame3=pd.DataFrame(pop)
frame3


# In[20]:


frame3.T


# In[21]:


pd.DataFrame(pop, index=[2001,2002,2003])


# In[22]:


frame3.index.name='year';frame3.columns.name='state'
frame3


# In[23]:


frame3.values


# In[24]:


frame2.values


# In[ ]:




