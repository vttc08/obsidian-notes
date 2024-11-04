#!/usr/bin/env python
# coding: utf-8

# Tqdm Progress Bar

# In[8]:


from tqdm import tqdm, trange
import time


# In[4]:


for _ in tqdm(range(100)):
    time.sleep(0.01)
    pass


# tqdm function takes a list or iterable as an argument
# trange is a tqdm replacement for the range function

# In[11]:


# tqdm looping
mylist = [1, 2, 3, 4, 5]
for i in tqdm(mylist):
    time.sleep(0.2)
# trange
for i in trange(1000000):
    pass


# total is an argument to tqdm function which is used to specify the total number of iterations
# other arguments include, description (desc), units(unit)

# In[14]:


for i in tqdm(mylist, total=8, desc="My Progress Bar", unit="item"): # progress bar will not complete
    # if the total is less than actual length, the progress bar will show until the total
    time.sleep(0.2)


# In[17]:


# Nested progress bars
for i in trange(2):
    for j in trange(3):
        time.sleep(0.5)


# a tqdm object eg. pbar can be created for dynamic progress bar

# In[ ]:


pbar = tqdm(range(20))
for i in pbar:
    time.sleep(0.1)
    pbar.set_description("Processing %s" % i)
pbar.close()


# In[37]:


import random
randomcolor = ['red', 'green', 'yellow', 'blue', 'magenta', 'cyan', 'white']
pbar = tqdm(range(100), ncols=100, mininterval=0.5)
for i in pbar:
    time.sleep(0.1)
    pbar.colour = random.choice(randomcolor)

