Tqdm Progress Bar


```python
from tqdm import tqdm, trange
import time
```


```python
for _ in tqdm(range(100)):
    time.sleep(0.01)
    pass
```

    100%|██████████| 100/100 [00:01<00:00, 63.43it/s]
    

tqdm function takes a list or iterable as an argument
trange is a tqdm replacement for the range function


```python
# tqdm looping
mylist = [1, 2, 3, 4, 5]
for i in tqdm(mylist):
    time.sleep(0.2)
# trange
for i in trange(1000000):
    pass
```

    100%|██████████| 5/5 [00:01<00:00,  4.92it/s]
    100%|██████████| 1000000/1000000 [00:00<00:00, 8937057.33it/s]
    

total is an argument to tqdm function which is used to specify the total number of iterations
other arguments include, description (desc), units(unit)


```python
for i in tqdm(mylist, total=8, desc="My Progress Bar", unit="item"): # progress bar will not complete
    # if the total is less than actual length, the progress bar will show until the total
    time.sleep(0.2)
```

    My Progress Bar:  62%|██████▎   | 5/8 [00:01<00:00,  4.87item/s]
    


```python
# Nested progress bars
for i in trange(2):
    for j in trange(3):
        time.sleep(0.5)
```

    100%|██████████| 3/3 [00:01<00:00,  1.96it/s]
    100%|██████████| 3/3 [00:01<00:00,  1.95it/s]
    100%|██████████| 2/2 [00:03<00:00,  1.54s/it]
    

a tqdm object eg. pbar can be created for dynamic progress bar


```python
pbar = tqdm(range(20))
for i in pbar:
    time.sleep(0.1)
    pbar.set_description("Processing %s" % i)
pbar.close()
```

    Processing 19: 100%|██████████| 20/20 [00:02<00:00,  9.12it/s]
    


```python
import random
randomcolor = ['red', 'green', 'yellow', 'blue', 'magenta', 'cyan', 'white']
pbar = tqdm(range(100), ncols=100, mininterval=0.5)
for i in pbar:
    time.sleep(0.1)
    pbar.colour = random.choice(randomcolor)
```

    100%|[33m█████████████████████████████████████████████████████████████[0m| 100/100 [00:10<00:00,  9.11it/s][0m
    
