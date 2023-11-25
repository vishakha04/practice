#!/usr/bin/env python
# coding: utf-8

# In[11]:


height= float(input("enter your height in cms: "))
age = int(input("Enter your age: "))
price=0

if(height>=120):
    print("Congratulations! You can buy the ticket.")
    if(age<12):
        print("Tickets for children costs Rs. 50")
        price=50
    if(age<=18):
        print("Tickets for youth costs Rs. 80")
        price=80
    else:
        print("Tickets for adult costs Rs. 100")
        price=100
    photos=input("Do you want to buy the photographs? Y/N\n")

    if(photos=="Y" or photos=="y"):
        price+= 30
    print(f"Final ticket price is: {price}")
    elif(photos=="N" or photos=="n"):
        total = price
        print(f"Final ticket price is: {total}")
    else:
        print("please make a valid selection.")
        
else:
    print("Try again next year.")


# In[ ]:





# In[ ]:




