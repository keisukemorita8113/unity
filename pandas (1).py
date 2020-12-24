#!/usr/bin/env python
# coding: utf-8

# In[4]:


import pandas as pd


# In[5]:


df = pd.DataFrame([[1,2,3],[4,5,6,],[7,8,9]],
                 columns = ['col01','col02','col03'],
                 index= ['idx01','idx02','idx03'])
df


# In[6]:


import numpy as np


# In[7]:


df = pd.DataFrame(np.array([[1,2,3],[4,5,6,],[7,8,9]]),
                 columns = ['col01','col02','col03'],
                 index= ['idx01','idx02','idx03'])
df


# In[8]:


df.index


# In[9]:


df.columns


# In[10]:


df = pd.DataFrame({'col01':[1,2,3],
                   'col02':[4,5,6,],
                   'col03':[7,8,9]}
                  ,index=['idx01','idx02','idx03'])
df


# In[11]:


#普通の作成方法
df = pd.DataFrame([[1,2,3],
                   [4,5,6,],
                   [7,8,9]])
df                


# In[12]:


# カラム名とINDEXをつける
df.columns=['col01','col02','col03']
df.index=['idx01','idx02','idx03']


# In[13]:


df


# In[14]:


df['col01']


# In[15]:


df.loc['idx01']


# In[17]:


df.loc['idx02','col02']


# In[19]:


df.loc['idx02','col02']=100
df


# In[20]:


# :は全ての意味
df.loc[:,'col03']=['Tokyo','Osaka','Hokkaido']
df


# In[21]:


# 複数行取得
df.iloc[:,1:3]


# In[ ]:




