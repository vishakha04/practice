#!/usr/bin/env python
# coding: utf-8

# In[2]:


print("Welcome to tip calculator")


# In[1]:


bill=float(input("what is your total bill?\nRs."))


# In[2]:


tip=int(input("what percentage tip would you want to tip your waiter? 10%, 12%, 20%\n"))


# In[3]:


num=int(input("how many people are splitting this bill?\n"))


# In[4]:


t=(bill*tip)/100
print(t)


# In[7]:


split=round((bill + t)/num,2)
print(f"each person should pay :Rs.",split)


# In[ ]:




