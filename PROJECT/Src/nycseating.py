#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd


# In[2]:


benches = pd.read_csv('/Users/oliviam/Desktop/bench.csv')


# In[7]:


benches.head()


# In[15]:


newdf = benches.drop(["the_geom", "BoroCD", "CongDist", "CounDist", "AssemDist", "StSenDist", "CongDist", "SiteID", "BenchID", "ComDist", "Installati", "Latitude", "Longitude", "Street", "CrossStree", "BID", "BusRoute", "FEMAFldz", "FEMAFldT", "HrcEvac" ], axis='columns')


# In[16]:


newdf.shape


# In[29]:


bronx_div = ['Bronx']
bronx_div = newdf.loc[newdf['BoroName'].isin(bronx_div)]
bronx_div.to_csv('bronx_div_df.csv')


# In[30]:


brooklyn_div = ['Brooklyn']
brooklyn_div = newdf.loc[newdf['BoroName'].isin(brooklyn_div)]
brooklyn_div.to_csv('brooklyn_div_df.csv')


# In[31]:


man_div = ['Manhattan']
man_div = newdf.loc[newdf['BoroName'].isin(man_div)]
man_div.to_csv('man_div_df.csv')


# In[32]:


benches2 = pd.read_csv('/Users/oliviam/Desktop/man_div_df.csv')


# In[37]:


benches2.loc[benches2['BenchType'] == 'backless']


# In[58]:


seating = pd.read_csv('/Users/oliviam/Desktop/Seating_Locations.csv')


# In[59]:


seating.loc[seating['SeatingTyp'] == 'LEANING BAR']


# In[44]:


newdfseat = seating.drop(["the_geom", "BoroCD", "CongDist", "CounDist", "AssemDist", "StSenDist", "CongDist", "SiteID", "ComDist", "Installati", "Latitude", "Longitude", "Street", "CrossStree", "BID", "BusRoute", "FEMAFldz", "FEMAFldT", "HrcEvac" ], axis='columns')


# In[49]:


newdfseat.loc[newdfseat['BoroName'] == 'Manhattan']


# In[53]:


man_div2 = ['Manhattan']
man_div2 = newdfseat.loc[newdfseat['BoroName'].isin(man_div2)]
man_div2.to_csv('man_div_df2.csv')


# In[54]:


bars = pd.read_csv('/Users/oliviam/Desktop/man_div_df2.csv')


# In[56]:


bars.head()


# In[57]:


bars.loc[bars['SeatingTyp'] == 'LEANING BAR']


# In[ ]:




