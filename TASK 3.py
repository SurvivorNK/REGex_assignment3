#!/usr/bin/env python
# coding: utf-8

# # Task 3
# 
# # Registration Id:SIRSS2272
# 
# # Name: Nishant Kumar

# Q1. Write a function to return nth term of Fibonacci sequence.

# In[6]:


num=int(input('enter the nth term of series'))
def fibo(num):
    if num==0:
        return 0
    elif num==1:
        return 1
    else:
        return (fibo(num-2)+fibo(num-1))
print( fibo(num-2)+fibo(num-1))


# 
# Q2. Write a function to find out GCD of two numbers using EUCLID'S algorithm

# In[7]:


def gcd(n1, n2):
    while n1 != 0 and n2 != 0:
        x = n1 % n2
        n1 = n2
        n2 = x
    if  n1== 0:
        print('GCD is', n2)
    else:
        print('GCD is', n1)

n1 = int(input('Enter the first number '))
n2 = int(input('Enter the second number '))
if n1 > n2:
    n1 = n1
    n2 = n2
    gcd(n1, n2)
elif n1 < n2 :
    a = n1
    n1 = n2
    n2 = a
    gcd(n1, n2)
else :
    print('Both numbers are equal')


# Q3. Write a function to find LCM of two number in most optimizers way.

# In[8]:


n1=int(input("Enter first number:"))
n2=int(input("Enter second number:"))
j=max(n1,n2)
while(True):
    if (j%n1==0) and (j%n2==0):
        result=j
        break
    else:
        j=j+1

print("LCM of {0} and {1} is {2}".format(n1,n2,result))


# In[ ]:




