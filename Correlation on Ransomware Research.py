#!/usr/bin/env python
# coding: utf-8

# In[1]:


from string import ascii_letters
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


# In[2]:


sns.set_theme(style="white")


# In[4]:


df = pd.read_csv("https://raw.githubusercontent.com/tahlla-utd/cybersecresearch/main/CyberResearch.txt", sep = ';')


# In[6]:


corr = df.corr()


# In[7]:


mask = np.triu(np.ones_like(corr, dtype=bool))


# In[9]:


f, ax = plt.subplots(figsize=(11, 9))

cmap = sns.diverging_palette(230, 20, as_cmap=True)

sns.heatmap(corr, mask=mask, cmap=cmap, vmax=.3, center=0,
            square=True, linewidths=.5, cbar_kws={"shrink": .5})

