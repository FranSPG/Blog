#!/usr/bin/env python
# coding: utf-8

# In[1]:


import sys
sys.setrecursionlimit(100000000)


# In[2]:


def fib(n):
    if n == 0 or n == 1:
        return 1
    else:
        return fib(n - 1) + fib(n - 2)


# In[ ]:


get_ipython().run_cell_magic('time', '', "for i in range(50):\n    print('fib(' + str(i) + ') =', fib(i))")


# In[3]:


# la función tiene un argumento más que la anterior
# memo es el diccionario donde se van a ir guardando las operaciones y su resultado
def fastFib(n, memo = {}):
    """Assumes n is an int >= 0, memo used only by recursive calls
       Returns Fibonacci of n"""
    if n == 0 or n == 1:
        return 1
    try:
        # Primero intenta devolver el valor si esta almacenado en el memo
        return memo[n]
    except KeyError:
        # Si no está en memo computa el resultado y lo guarda en el memo
        result = fastFib(n-1, memo) + fastFib(n-2, memo)
        memo[n] = result
        return result


# In[4]:


get_ipython().run_cell_magic('time', '', 'fastFib(60)')

