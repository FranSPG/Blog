#!/usr/bin/env python
# coding: utf-8

# In[1]:


import imageio
import glob
import natsort
import re


# In[2]:


images = []

filenames = [img for img in glob.glob("rfft/*.jpg")]

filenames.sort(key=lambda var:[int(x) if x.isdigit() else x for x in re.findall(r'[^0-9]|[0-9]+', var)])


for image_path in filenames:
    images.append(imageio.imread(image_path))
    images.append(imageio.imread(image_path))
    images.append(imageio.imread(image_path))
    images.append(imageio.imread(image_path))
    images.append(imageio.imread(image_path))
    images.append(imageio.imread(image_path))


# In[3]:


imageio.mimsave('rfft.gif', images)


# In[ ]:




