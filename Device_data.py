#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd


# In[2]:


phone_data = 'used_device_data.csv'

df_data = pd.read_csv(phone_data)

df_data.head()


# In[3]:


# Function to sort the dataframe based:brand_name,os,screen_size,4g,5g,int_memory,ram,battery,weight,release_year
def sort_data():
    return df_data.sort_values(by = ['brand_name','os','screen_size','4g','5g','int_memory','ram','battery','weight','release_year'],na_position = 'first',ignore_index=True)
sort_data()


# In[4]:


# Lets create a mask/filter of all cell phones with null in main_camera_mp
def create_mask():
    df_filter = sort_data()
    
    return df_filter[df_filter['main_camera_mp'].isnull()]
# A total of 179 cell phones have no values in the main_camera_mp column
create_mask()


# In[5]:


# lets create a function to fill all the 179 null values for main_camera_mp
def fill_na():
    new_df = sort_data()
    new_df[['main_camera_mp']] = new_df[['main_camera_mp']].fillna(method = 'ffill',axis=0)
    return new_df
fill_na()


# In[6]:


def check_if_nulls_exist():
    df_new = fill_na()
    
    return df_new[df_new['main_camera_mp'].isnull()]
# This should return zero columns
check_if_nulls_exist()


# ### Write final data to csv

# In[7]:


df_to_csv = fill_na()
df_to_csv.to_csv('New_Phone_Data.csv')

