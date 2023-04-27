#!/usr/bin/env python
# coding: utf-8

# In[2]:


import numpy as np 
import pandas as pd 
import matplotlib.pyplot as plt
from builtins import list
import matplotlib
matplotlib.style.use('ggplot')
import datetime
get_ipython().run_line_magic('matplotlib', 'inline')
from subprocess import check_output


# In[3]:


uber_df=pd.read_csv("Uber-dataset.csv")


# In[4]:


uber_df.head()


# In[5]:


uber_df.tail()


# In[6]:


uber_df = uber_df[:-1]


# In[10]:


def convert_time(column_name):
    y=[]
    for x in uber_df[column_name]:
        y.append(datetime.datetime.strptime(x, "%m/%d/%Y %H:%M"))

    uber_df[column_name] = y


# In[11]:


column_date=uber_df[['START_DATE*','END_DATE*']] 
for x in column_date:
    convert_time(x)


# In[12]:


uber_df.info()


# In[13]:


x = uber_df['CATEGORY*'].value_counts().plot(kind='bar')


# In[14]:


count = 0
month=[]
while count < len(uber_df):
    month.append(uber_df['START_DATE*'][count].month)
    count = count+1
uber_df['Month'] = month


# In[15]:


minutes=[]
uber_df['Duration_Minutes'] = uber_df['END_DATE*'] - uber_df['START_DATE*']
uber_df['Duration_Minutes']
for x in uber_df['Duration_Minutes']:
    minutes.append(x.seconds / 60)

uber_df['Duration_Minutes'] = minutes


# In[16]:


x = uber_df['Month'].value_counts()
x.plot(kind='bar',figsize=(10,5),color='orange')
plt.xlabel('Month')
plt.ylabel('Frequency')
plt.title('Number of trips per Month')


# In[17]:


hours = uber_df['START_DATE*'].dt.hour.value_counts()
hours.plot(kind='bar',color='orange',figsize=(10,5))
plt.xlabel('Hours')
plt.ylabel('Frequency')
plt.title('Number of trips per hour')


# In[18]:


purpose_time = uber_df['PURPOSE*'].value_counts()
purpose_time.plot(kind='bar',figsize=(10,5),color='green')


# In[19]:


purpose = uber_df.groupby('PURPOSE*').mean()
purpose.plot(kind = 'bar',figsize=(15,5))


# In[20]:


uber_df['Duration_hours'] = uber_df['Duration_Minutes'] / 60
uber_df['Speed_KM'] = uber_df['MILES*'] / uber_df['Duration_hours']
uber_df['Speed_KM']


# In[ ]:




