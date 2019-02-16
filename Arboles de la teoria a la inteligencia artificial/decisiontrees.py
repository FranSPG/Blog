#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd

from sklearn.model_selection import cross_val_score
from sklearn.metrics import accuracy_score
from sklearn.ensemble import RandomForestClassifier, BaggingClassifier
from sklearn import model_selection
from sklearn.preprocessing import LabelEncoder
from sklearn import tree
from sklearn import metrics
import os
os.environ["PATH"] += os.pathsep + 'C:/Program Files (x86)/Graphviz2.38/bin/'

import graphviz
import pydot


# In[2]:


df = pd.read_csv('data.csv', index_col=0)
df.drop('Unnamed: 32', axis=1, inplace=True)


# In[3]:


df.head()


# In[4]:


target = 'diagnosis'
cols = df.columns[df.columns != 'diagnosis']


# In[5]:


train_x, test_x, train_y, test_y = model_selection.train_test_split(df[cols], 
                                                                    df[target],
                                                                    test_size=.3)


# In[6]:


tree_classifier = tree.DecisionTreeClassifier(criterion='gini', min_samples_split=23)

tree_classifier = tree_classifier.fit(train_x, train_y)


# In[7]:


print(accuracy_score(test_y, tree_classifier.predict(test_x)))


# In[8]:


dot_data = tree.export_graphviz(tree_classifier, out_file=None) 

graph = graphviz.Source(dot_data) 
graph.render("treecls") 


# In[9]:


dot_data = tree.export_graphviz(tree_classifier, out_file=None, 
                     feature_names=df[cols].columns,  
                     class_names=df[target].unique(),  
                     filled=True, rounded=True,  
                     special_characters=True)  
graph = graphviz.Source(dot_data)  
graph 


# In[10]:


from sklearn.metrics import confusion_matrix
import matplotlib.pyplot as plt
import seaborn as sns


cm = confusion_matrix(test_y, tree_classifier.predict(test_x))
# True Positives
TP = cm[1, 1]

# True Negatives
TN = cm[0, 0]

# False Positives
FP = cm[0, 1]

# False Negatives
FN = cm[1, 0]


# In[11]:


ax= plt.subplot()
sns.heatmap(cm, annot=True, ax = ax, fmt='g') 

# labels, title and ticks
ax.set_xlabel('Predicted labels')
ax.set_ylabel('True labels')
ax.set_title('Confusion Matrix')
ax.xaxis.set_ticklabels(['Benigno', 'Maligno'])
ax.yaxis.set_ticklabels(['Benigno', 'Maligno'])
plt.savefig('breastconfusionmatrix.jpg')


# In[ ]:




