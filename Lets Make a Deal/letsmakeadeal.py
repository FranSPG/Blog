#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
from tqdm import tqdm
import time


# In[2]:


def no_change():
    
    # Doors
    doors = [False, False, False]

    # Generate one winner door randomly
    winner_door = np.random.randint(0, 3)
    doors[winner_door] = True

    # Select one door randomly
    selected_door = np.random.randint(0, 3)
    
    # Just cheecking if the selected door is the winner door
    if(winner_door == selected_door):
        rst = True
    else:
        rst = False
        
    #print("Selected door: {}\t Winning door: {}\t Result: {}\n".format(selected_door, selected_door, rst))
    
    return rst


# In[3]:


def change():
    
    # Doors
    doors = [False, False, False]

    # Generate one winner door randomly
    winner_door = np.random.randint(0, 3)
    doors[winner_door] = True

    # Select one door randomly
    selected_door = np.random.randint(0, 3)
    
    # Searching the remaining door to show
    for x in range(0, 3):
        
        if (doors[x] == True):
            pass
        else:
            if (x != selected_door):
                door_shown = x
    
    # Changing the first selection 
    for x in range(0, 3):
        if (x == door_shown):
            pass
        else:
            if(x != selected_door):
                new_door = x

    # Just cheecking if the selected door is the winner door
    if(winner_door == new_door):
        rst = True
    else:
        rst = False
        
    #print("Selected door: {}\t Door shown: {}\tNew door: {}\t Winning door: {}\t Result: {}\n".format(selected_door, door_shown, new_door, winner_door, rst))
    
    return rst


# In[4]:


no_change_mean = np.array([])
for x in tqdm(range(100)):
    no_change_rst = []
    for i in range(200000):
        no_change_rst.append(no_change())
    
    no_change_rst = sum(no_change_rst)
    no_change_mean = np.append(no_change_mean, no_change_rst)


# In[5]:


change_mean = np.array([])
for x in tqdm(range(100)):
    change_rst = []
    for i in range(20000):
        change_rst.append(change())
    
    change_rst = sum(change_rst)
    change_mean = np.append(change_mean, change_rst)


# In[6]:


print("Mean of winning rounds in 200000 with no change of doors: {}\n".format(np.mean(no_change_mean)))

print("Clearly we can see that 200000 * (1/3) = 66666.666 is very closely to the result\n")


# In[7]:


print("Mean of winning rounds in 200000 with change of doors: {}\n".format(np.mean(change_mean)))

print("Clearly we can see that 200000 * (2/3) = 133333.333 is very closely to the result\n")


# In[ ]:




