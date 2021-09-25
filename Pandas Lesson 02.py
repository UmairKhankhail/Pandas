#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import pandas as pd


# In[2]:


'python -m pip install --upgrage pip'


# In[3]:


print('xlrd installed')


# In[4]:


can_imm=pd.read_csv('D:\Data Science\Data Analytics Sir Shoaib\immigration to Canada.csv')


# In[5]:


can_imm.head()


# In[6]:


can_imm.tail()


# In[7]:


can_imm.info


# In[8]:


can_imm.info(verbose=False)


# In[9]:


can_imm.columns


# In[10]:


type(can_imm.columns)


# In[11]:


can_imm.columns.values


# In[12]:


print(type(can_imm.columns.values.tolist()))


# In[30]:


can_imm.isnull().sum()


# In[13]:


print(type(can_imm.columns.tolist()))


# In[14]:


can_imm.index.values


# In[15]:


can_imm.head(2)


# In[16]:


can_imm.drop(['AREA','REG','DEV','Type','Coverage'],axis=1,inplace=True)


# In[17]:


can_imm.head(2)


# In[18]:


can_imm.rename(columns={'OdName':'Country','AreaName':'Continent','RegName':'Region'},inplace=True)


# In[19]:


can_imm.head(2)


# In[20]:


can_imm.index


# In[21]:


can_imm.columns


# In[22]:


can_imm['Total']=can_imm.sum(axis=1)
can_imm.head(2)


# In[33]:


can_imm.describe()


# In[34]:


can_imm.columns


# In[35]:


can_imm.columns.values


# In[36]:


can_imm.Country


# In[52]:


#Method 01 
#def.columnname  no special caracter
#returns series
#Method 02
#def.columnname[['column','column1']]
#return dataframe


# In[53]:


can_imm['Country']


# In[54]:


can_imm['Country','Continent']


# In[60]:


can_imm[['Country','Continent','1980']]


# In[62]:


can_imm.set_index('Country')


# In[65]:


can_imm.reset_index()


# In[75]:


can_imm.drop('Country',axis=1)


# In[76]:


can_imm


# In[77]:


can_imm.set_index('Country',inplace=True)


# In[78]:


can_imm


# In[82]:


can_imm.loc['Brazil']


# In[84]:


can_imm.loc['Afghanistan']


# In[86]:


can_imm.loc['china']


# In[23]:


can_imm.iloc[22]


# In[24]:


can_imm.iloc[20]


# In[25]:


can_imm.iloc[50]


# In[34]:


can_imm.set_index('Country',inplace=True)


# In[35]:


can_imm


# In[36]:


can_imm[can_imm.index=='Brazil']


# In[37]:


can_imm[can_imm.index=='Brazil'].T.squeeze()


# In[41]:


can_imm.loc['Brazil','2013']


# In[44]:


can_imm.iloc[22,36] #row index and column index


# In[45]:


can_imm


# In[46]:


can_imm.head(1)


# In[54]:


can_imm


# In[63]:


can_imm.loc['Afghanistan',['1980','1981','1982','1983','1984','1985']]


# In[55]:


can_imm.loc['Afghanistan']


# In[67]:


can_imm.iloc[22,[3,4,5,6,7,8]]


# In[68]:


#To convert all the columns into string

can_imm.columns=list(map(str,can_imm.columns))


# In[69]:


years=list(map(str,range(1980,2014)))


# In[70]:


years


# In[75]:


condition=can_imm['Continent']=='Asia'


# In[76]:


condition


# In[77]:


can_imm[condition]


# In[78]:


condition=can_imm['Continent']=="Africa"


# In[79]:


condition


# In[80]:


can_imm[condition]


# In[83]:


condition1= (can_imm['Continent']=='Asia') & (can_imm['Region']=='Southern Asia')


# In[84]:


condition1


# In[85]:


can_imm[condition1]


# In[86]:


can_imm.shape


# In[87]:


can_imm.index


# In[88]:


can_imm.index.values


# In[89]:


can_imm.columns


# In[ ]:




