#!/usr/bin/env python
# coding: utf-8

# In[1]:


year = int(input())

if(year%4 == 0):
  if (year%100 ==0):
    if(year%400==0):
      print("Leap year")
    else:
      print("Not leap year")
  else:
    print("Leap year")
else:
  print("Not leap year")


# In[ ]:




