#!/usr/bin/env python
# coding: utf-8

# # Assignment 5 Sort it in ascending order but all zeros should be at right hand side.

# In[6]:


List = [0,1,2,10,4,1,0,56,2,0,1,3,0,56,0,4]
List.sort()
c=List.count(0)
print(List[c:]+List[:c])


# # 2) Merge two lists & produce one sorted list .

# In[7]:


list1=[1,5,3,2,4]
list2=[7,10,8,6,9]
list3=list1+list2
list4=[]
for num in range(min(list3),max(list3)+1):
    if num in list3:
        list4.append(num)
print(list4)

