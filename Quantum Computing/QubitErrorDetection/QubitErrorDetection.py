#!/usr/bin/env python
# coding: utf-8

# In[203]:


import numpy as np
import itertools as it
import math


# In[2]:


g_binary = np.array([[1,1,0],[1,0,1],[0,1,1]])

g = np.hstack((np.identity(3), g_binary)).astype(int)


# In[9]:


print(g)


# In[10]:


g_binary_t = np.array(g_binary.T)


# In[13]:


print(g_binary_t)


# In[14]:


h = np.hstack((g_binary_t, np.identity(3))).astype(int)


# In[15]:


print(h)


# In[22]:


ht = np.array(h.T).astype(int)


# In[24]:


print(ht)


# In[7]:


ortogonalidad = xor_matrix(np.matmul(g, h.T))
print(ortogonalidad)


# In[3]:


def xor_matrix(matr):
    """
        function to apply xor gate to a matrix given.
    """
    matr = np.array(matr)
    
    if(matr.shape[0] == 1):
        for idx, i in enumerate(matr[0]):
            if(matr[0][idx] %2 == 0):
                matr[0][idx] = 0
            else:
                matr[0][idx] = 1
            
    else:
        for idx, arr in enumerate(matr):
            for idx1, arr1 in enumerate(arr):
                if(matr[idx][idx1] %2 == 0):
                    matr[idx][idx1] = 0
                else:
                    matr[idx][idx1] = 1
    
    return matr


# In[28]:


binar = np.array(list(it.product([0, 1], repeat=3)))


# In[29]:


print(binar)


# In[5]:


codes = np.matmul(binar, g)

codes = xor_matrix(codes)


print(codes)


# In[31]:


code_recived = [1,0,1,0,0,0]
error_detect = xor_matrix(np.array([np.matmul(code_recived, h.T)]))

print(error_detect)


# <h1>Quantum Bits</h1>

# In[32]:


one = [0, 1]
zero = [1, 0]


# In[75]:


qcombs = np.array(list(it.product([zero, one], repeat=2)))


# In[84]:


kron_prod = []
for i in qcombs:
    kron = i[0]
    for x in range(1, len(i)):
        kron = np.kron(kron, i[x])
    print("\n")
    print(kron)
    
    kron_prod.append(kron)
    
kron_prod = np.array(kron_prod)


# In[137]:


#qg_binary = np.array([[1,1,0],[1,0,1],[0,1,1], [1,1,1]])
qg_binary = np.array([[1,1],[1,0],[0,1],[0,0]])

qg = np.hstack((np.identity(4), qg_binary)).astype(int)


# In[161]:


print(qg)


# In[139]:


qg_binary_t = np.array(qg_binary.T)


# In[140]:


print(qg_binary_t)


# In[144]:


qh = np.hstack((qg_binary_t, np.identity(2))).astype(int)


# In[145]:


print(qh)


# In[146]:


qht = np.array(qh.T).astype(int)


# In[147]:


print(qht)


# In[148]:


qortogonalidad = xor_matrix(np.matmul(qg, qh.T))
print(qortogonalidad)


# In[149]:


qcodes = np.matmul(kron_prod, qg)

qcodes = xor_matrix(qcodes)


print(qcodes)


# In[242]:


print(kron_prod)
print(qg)


# In[164]:


qcode_recived = [0,0,0,0,1,1]
qerror_detect = xor_matrix(np.array([np.matmul(qcode_recived, qht)]))

print(qerror_detect)


# In[235]:


hadamard = np.array([[1/math.sqrt(2), 1/math.sqrt(2)],[1/math.sqrt(2), -(1/math.sqrt(2))]]).astype(float)


# In[236]:


hadamard


# In[237]:


zero_had = np.matmul(zero, hadamard)


# In[238]:


zero_had


# In[239]:


kron_had = np.array(np.kron(zero_had, zero_had))


# In[240]:


print(kron_had)


# In[ ]:




