#!/usr/bin/env python
# coding: utf-8

# In[ ]:


def add(a,b):
        return a+b
def sub(a,b):
        return a-b
def mul(a,b):
     return a*b
def div(a,b):
         return a/b
def mod(a,b):
        return a%b
print("menu")
print("1)addition")
print("2)subtraction")
print("3)muliplication")
print("4)division")
print("5)modulo division")
while True:
    choice=input("enter your choice")
    n1=float(input("enter the first number"))
    n2=float(input("enter the second number"))
    if choice=='1':
        print(n1,"+",n2,"=",add(n1,n2))
    elif choice=='2':
        print(n1,"-",n2,"=",sub(n1,n2))
    elif choice=='3':
        print(n1,"*",n2,"=",mul(n1,n2))
    elif choice=='4':
        print(n1,"/",n2,"=",div(n1,n2))
    elif choice=='5':
        print(n1,"%",n2,"=",mod(n1,n2))
    else:
        print("invalid option")
    x=input("do you want to continue")
    if x=="n":
         break
            
    
    
    
   


# In[ ]:





# In[ ]:




