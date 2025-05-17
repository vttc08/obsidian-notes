```python
import threading
import time
```

```python
def do_something():
    print("Doing something...\n")
    time.sleep(2)
    print("Done!\n")
```

```python
do_something()
do_something()
# this code will take 4 seconds to run
# because it runs the function twice in a row
print("Done")
```

## Basic Threading

```python
t1 = threading.Thread(target=do_something) # pass the function, not execute it
t2 = threading.Thread(target=do_something)
```

```python
# start the threads
t1.start()
t2.start()
```

Now the t1 and t2 threads are running in parallel. But anything after the `start()` method in the main thread will not wait for t1 and t2 to finish.

```python
t1.start() # start the first thread
t1.join() # wait for it to finish
print("Done") # will wait for t1 to finish before printing
```

Adding arguments to threading

```python
def func(x):
    print(x)
    time.sleep(2)

# uses the argss/kwargs to pass arguments to the function
t1 = threading.Thread(target=func, args=(1,))
t2 = threading.Thread(target=func, kwargs={'x': 2})
```

Daemon threads
- this will run in the background and stop when the main program exits

```python
dt = threading.Thread(target=do_something, daemon=True) # this thread will not block the program from exiting
```

## Threading with For Loop
By appending threads to a list, similar to asyncio gather.

```python
threads = []

# append the threads to a list
for _ in range(10):
    t = threading.Thread(target=do_something)
    t.start() # start the thread
    threads.append(t) # add the thread to the list

# start all threads
for thread in threads:
    thread.join() # wait for all threads to finish
print("Done") # will wait for all threads to finish before printing
```

## Threadpool Executor

```python
import concurrent.futures
```

```python
with concurrent.futures.ThreadPoolExecutor() as executor:
    f1 = executor.submit(func, x=1) # submit the function to the thread pool with arguments
    # returns a Future object
    f1.result() # wait for the result of the function to finish
```

    1

```python
with concurrent.futures.ThreadPoolExecutor() as executor:
    results = [executor.submit(func, x) for x in range(10)] # submit the function to the thread pool with arguments
    # this returna list of Future objects
    for f in concurrent.futures.as_completed(results): # wait for the results t o finish
        print(f.result()) # print the result of the function
```

```python
# executor.map()
with concurrent.futures.ThreadPoolExecutor() as executor:
    mylist = [1, 2, 3, 4, 5]
    results = executor.map(func, mylist) # submit the function to the thread pool with arguments
    # takes and iterable and returns an iterator of results
    # e.g. func(1), func(2), func(3), func(4), func(5) into the thread pool
    for result in results: # wait for the results to finish
        print(result) # print the result of the function
```
