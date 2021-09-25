#!/usr/bin/env python
# coding: utf-8

# In[7]:


pip install pandas


# In[8]:


import matplotlib.pyplot as pt #scripting interface
get_ipython().run_line_magic('matplotlib', 'inline')
import pandas as pd
import os


# In[9]:


'pip - m pip install --upgrade pip'


# In[10]:


print('xlrd installed')


# In[22]:


a_price=pd.read_csv(r"D:\Data Science\Data Analytics Sir Shoaib\areas price.csv")
a_price.head()


# In[23]:


a_price.tail()


# In[25]:


a_price.tail(3)


# In[27]:


a_price.shape


# In[28]:


a_price.info


# In[31]:


a_price.info(verbose=False)


# In[33]:


a_price.describe()


# In[34]:


a_price.index


# In[35]:


a_price.values


# In[36]:


a_price.columns


# In[37]:


a_price.columns.values


# In[41]:


print(type(a_price.columns))
print(type(a_price.columns.values))


# In[44]:


a_price.columns.tolist
a_price.columns.values.tolist
print(type(a_price.columns.tolist))
print(type(a_price.columns.values.tolist))


# In[ ]:




