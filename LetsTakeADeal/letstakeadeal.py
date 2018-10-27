#!/usr/bin/env python
# coding: utf-8

# In[9]:


import numpy as np


# In[10]:


def no_change():
    
    doors = [False, False, False]

    doors[np.random.randint(0, 3)] = True

    selected_door = np.random.randint(0, 3)
    
    for x in range(0,3):
        
        if (doors[x] == True):
            winner_door = x
        else:
            if (x != selected_door):
                door_shown = x
        
    if(winner_door == selected_door):
        rst = True
    else:
        rst = False
        
    #print("Selected door: {}\t Door shown: {}\t Winning door: {}\t Result: {}\n".format(selected_door, door_shown, selected_door, rst))
    
    return rst


# In[11]:


def change():
    
    doors = [False, False, False]

    doors[np.random.randint(0, 3)] = True

    selected_door = np.random.randint(0, 3)
    
    for x in range(0, 3):
        
        if (doors[x] == True):
            winner_door = x
        else:
            if (x != selected_door):
                door_shown = x
    
    for x in range(0, 3):
        if (x == door_shown):
            pass
        else:
            if(x != selected_door):
                new_door = x
        
        
    if(winner_door == new_door):
        rst = True
    else:
        rst = False
        
    #print("Selected door: {}\t Door shown: {}\tNew door: {}\t Winning door: {}\t Result: {}\n".format(selected_door, door_shown, new_door, winner_door, rst))
    
    return rst


# In[12]:


b = np.array([])
for x in range(100):
    a = []
    for x in range(200000):
        a.append(no_change())
    
    a = sum(a)
    b = np.append(b, a)


# In[13]:


c = np.array([])
for x in range(100):
    d = []
    for x in range(200000):
        d.append(change())
    
    d = sum(d)
    c = np.append(c, d)


# In[14]:


np.mean(b)


# In[15]:


np.mean(c)


# In[ ]:




