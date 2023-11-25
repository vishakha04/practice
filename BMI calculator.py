#!/usr/bin/env python
# coding: utf-8

# In[2]:


height=float(input("Enter your height in meters: "))


# In[3]:


weight=float(input("Enter your weight in kgs: "))


# In[5]:


bmi= round(weight/(height**2),2)
print(bmi)


# In[6]:


print("your BMI is: ",bmi)
if(bmi<18.5):
  print("underweight")
elif(bmi>=18.5 and bmi<25):
  print("you have a normal weight")
elif(bmi>=25 and bmi<30):
  print("you are slightly overweight")
elif(bmi>=30 and bmi<35):
  print("you are obese")
elif(bmi>=35):
  print("you are clinically obese")
else:
  print("kindly re-enter the correct values.")


# In[ ]:




