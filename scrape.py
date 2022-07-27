#!/usr/bin/env python
# coding: utf-8

# # GitHub AutoScraper + history keeper

# ## This American Life

# In[1]:


import requests
from bs4 import BeautifulSoup
import pandas as pd
import re
import numpy as np


# In[2]:


response = requests.get("https://www.thisamericanlife.org/")
doc = BeautifulSoup(response.text, "html.parser")
# doc


# ## Episodes

# In[3]:


base_url = "https://www.thisamericanlife.org"


# ### Current episode

# In[4]:


current = []


# In[5]:


type = "Current"

num = re.findall(r'\d+', doc.find("a", class_="goto-episode").text)[0]
date = doc.find("span", "date-display-single").text
name = doc.find("h2").text
url = base_url + doc.find("article").a.get("href")
desc = doc.find("div", "field-type-text-with-summary").text.replace("View episode details", "")

episode_info = {
    "num": num,
    "date": date,
    "name": name,
    "url": url,
    "desc": desc,
    "type": type
}

current.append(episode_info)


# ### Recently aired episodes

# In[6]:


type = "Recently aired"

episodes = doc.find_all("article", class_="view-recently")

recent = []

for episode in episodes:
        
    num = episode.find("div", class_="field-name-field-episode-number").a.text
    url = base_url + episode.a.get("href")
    name = episode.find("h3").text
    date = episode.find("span", class_="date-display-single").text
    desc = episode.find("div", class_="field-type-text-with-summary").text.strip()
    
    episode_info = {
        "num": num,
        "date": date,
        "name": name,
        "url": url,
        "desc": desc,
        "type": type
    }
    
    recent.append(episode_info)


# In[12]:


combined = current + recent
print(combined)


# In[13]:


df = pd.DataFrame(combined)
df


# In[14]:


df.to_csv("episodes.csv", index=False)

