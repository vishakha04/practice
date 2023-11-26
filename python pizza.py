#!/usr/bin/env python
# coding: utf-8

# In[1]:


print("Thank you for choosing Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M, or L: ")
add_pepperoni = input("Do you want pepperoni? Y or N: ") 
extra_cheese = input("Do you want extra cheese? Y or N: ") 

bill=0

if(size == 'S'):
  bill +=500
elif(size == 'M'):
  bill +=650
elif(size == 'L'):
  bill += 800
else:
  print("please make a valid selection")
  
if(add_pepperoni=='Y'):
  if(size == 'S'):
    bill += 20
  else:
    bill +=30


if(extra_cheese=='Y'):
    bill += 10


print(f"Your final bill is: {bill}")


# In[ ]:




