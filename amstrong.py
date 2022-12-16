#!/usr/bin/env python
# coding: utf-8

# In[16]:


num=int(input("enter the number"))
temp=num
sum=0
while temp>0:
   digit=temp%10
   sum+=digit**3
   temp//=10
if num==sum:
        print("number is amstrong")
else:
        print("number is not amtsrong")
        


# In[ ]:




