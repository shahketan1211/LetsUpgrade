#!/usr/bin/env python
# coding: utf-8

# In[7]:


n = input("Enter Number to calculate sum")
n = int (n)
sum = 0
for num in range(0, n+1, 1):
    sum = sum+num
print("SUM of first ", n, "numbers is: ", sum )


# In[9]:


n = input("Enter Number to calculate sum")
n = int (n)
if n > 1:
   # check for factors
   for i in range(2,n):
       if (n % i) == 0:
           print(num,"is not a prime number")
           print(i,"times",n//i,"is",n)
           break
   else:
       print(n,"is a prime number")
       
# if input number is less than
# or equal to 1, it is not prime
else:
   print(n,"is not a prime number")

