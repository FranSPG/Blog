#!/usr/bin/env python
# coding: utf-8

# In[1]:


from sympy import *
import numpy as np


# In[2]:


x = Symbol('x')


# In[3]:


f = (x**x) - 100


# In[4]:


def f_x(f, x):
    return f.replace('x', x)


# In[5]:


def df(f):
    return f.diff()


# In[6]:


fprime = df(f)


# In[7]:


fprime


# In[8]:


def newtons_method(f, fprime, xn, eps, iteration):
    # Parámetros:
    # f : es la función
    # fprime : es la derivada de nuestra función
    # xn : es el valor o aproximación
    # eps : nos va a dar una toleracia de error
    # iteración : es un contador de iteraciones
    
    # Calculamos nuestro primer valor que le pasamos por xn
    # f_value va a tomar distintos valores a medida que se llama recursivamente a la función
    
    # f_x(f, xn) es una función donde le pasamos por parámetro la función (f) y el valor con el que
    # queremos reemplazar la x (en este caso xn) y nos retorna el resultado
    f_value = f_x(f, xn)
    
    if ((abs(f_value) > eps) and (iteration < 100)):
        
        try:
            # x_new Aplicamos nuestra formula y calculamos una nueva aproximación
            x_new = (xn - float((f_x(f, xn))) / float(f_x(fprime, xn)))
            
            # Llamamos recursivamente a la función pasandole los mismos parámetros, excepto que cambiamos xn por
            # nuestra nueva aproximación x_new y sumamos 1 a la iteración
            newtons_method(f, fprime, x_new, eps, iteration+1)
            
        
            # capturamos la expcepción de dividir por 0
        except ZeroDivisionError:
            print("Error! - derivative zero")
            
    else:
        
        # Mostramos el resultado
        print("\nf : {}\nfprime : {}\nxn : {}\neps : {}\niteration : {}".format(f, fprime, xn, eps, iteration))


# In[9]:


newtons_method(f, fprime, 2, 1.0e-6, 0)


# In[ ]:




