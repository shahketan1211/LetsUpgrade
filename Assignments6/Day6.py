#!/usr/bin/env python
# coding: utf-8

# # Convert to a dictionary in one line code using list comprehension

# In[1]:


list1=[1,2,3,4,5,7,8]
list2=["a","b","c","d","e"]


# In[2]:


list1 = [1, 2, 3,4, 5, 6, 7, 8]
list2 = ["a", "b", "c", "d", "e"]
for each in list1:
         list2.append((each))
print (list2)

