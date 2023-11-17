#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np


# In[8]:


index = ["Berlin", "Madrid", "Rom"]
bewölkerung  = pd.Series(data = [3.6, 3.3, 2.8], index = index)
fläche = pd.Series(data = [892, 604, 1285], index = index)
land = pd.Series(data = ["Deutschland", "Spanien", "Italien"], index = index)
sprache = pd.Series(data = ["deutsch", "spanisch", None], index = index)

my_dict = {
    'Bewölkerung': bewölkerung,
    'Fläche': fläche,
    'Land': land,
    'Sprache': sprache
}

df = pd.DataFrame(my_dict)
df.shape


# In[3]:


df.dtypes


# In[4]:


df.info()


# In[5]:


df.describe()


# In[6]:


df.isnull()


# In[7]:


df.isnull().sum()


# In[ ]:


#2 
df.iloc[2,3] = "italienisch"


# In[9]:


np.where(df.isna())


# In[14]:


index = ["New York"]
bewölkerung  = pd.Series(data = [8.5], index = index)
fläche = pd.Series(data = [700], index = index)
land = pd.Series(data = ["USA"], index = index)
sprache = pd.Series(data = ["englisch"], index = index)

my_dict2 = {
    'Bewölkerung': bewölkerung,
    'Fläche': fläche,
    'Land': land,
    'Sprache': sprache
}

df2 = pd.DataFrame(my_dict2)
df2


# In[16]:


df3 = pd.concat([df, df2])
df3.iloc[2,3] = "italienisch"
df3


# In[19]:


df3["EU"] = df3["Land"] != "USA"
df3


# In[21]:


df3["Region"] = np.where(df3["EU"] == True,  "Europe", "Americas")
df3

