#!/usr/bin/env python
# coding: utf-8

# In[50]:


list1 = [12,-7,5,64,-14]
list2 = [12,14,-95,3]
list=[]
for num in list1:
 if num>=0:
    print("\r", num)
for num in list2:
  if num>=0:
    list.append(num)
print(list)
    
   


# In[69]:


def printChar(arr,Len):
 occ={}
 for i in range(Len):
      if(arr[i] in occ):
           occ[arr[i]] = occ[arr[i]] + 1
      else:
            occ[arr[i]] = 1
 size = len(occ)
 while (size > 0):
     currentMax = 0
     arg_max = 0
     for key, value in occ.items():
            if (value > currentMax or (value == currentMax and key > arg_max)):
                arg_max = key
                currentMax = value
     print(f"{arg_max} - {currentMax}")
     occ.pop(arg_max)
     size -= 1
Str = "mississippi"
Len = len(Str)
printChar((Str), Len)


# In[ ]:




