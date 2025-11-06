# httpx
```bash
pip install httpx
```

```python

```

```python
import asyncio
async def main(): # This is a coroutine function
    print('Hello')
```

The asyncio doesn't work in Jupyter Notebook

```python
await main() # Use this for Jupyter notebook
```

```python
asyncio.run(main()) # This creates a new event loop and runs the coroutine
main() # this will return a coroutine object but not run
```

Coroutine object needs to be awaited or it won't execute.

# Awaitable objects
### Coroutine
Created by an asynchronous function.
```python
async def a(): # coroutine function
    pass
a() # => coroutine object
```
When awaiting a coroutine, it will run until completion, it does not yield control back to the event loop until it hits an `await` statement.

### Tasks
Created by calling `asyncio.create_task()` on a coroutine.
```python
task = asyncio.create_task(coro()) # => task object
task # => <Task pending ...>
await task # wait for the task to finish before continuing
task # => <Task finished ...>
```
When creating a tasks, it schedules it to run on the event loop.
### Future
A low-level awaitable object that represents a result that may not be available yet. Similar to a promise in JavaScript.

Async function with synchronous code
```python
async def sleeping():
    print("start")
    time.sleep(3) 
```
Use `await asyncio.to_thread()` to run the blocking code in a separate thread.
```python
async def main():
    task = asyncio.create_task(asyncio.to_thread(time.sleep, 3))
    task2 = asyncio.create_task(asyncio.to_thread(time.sleep, 2))
    await task
    await task2
```
This runs the blocking code in a separate thread, allowing the event loop to continue running other tasks while waiting for the blocking code to complete.

# Tasks
Tasks allow you to run multiple coroutines concurrently (run another coroutine while waiting for the first one to finish)

```python
# Create a task
task = asyncio.create_task(main())
task2 = asyncio.create_task(main())
await task
await task2
# wait for the task to finish before continuing
# but as soon as task is delayed, task2 can be run
```

```python
# Another way to create tasks is using gather
async def s(n):
    await asyncio.sleep(n)
    return n
await asyncio.gather(s(3), s(2), s(1)) # -> [3, 2, 1]
```

## gather
The `gather()` function can accept coroutine and tasks, runs concurrently and return a list.
- the coroutine just get result, while a task can be used to check the status of the task.
### exceptions
The `return_exceptions=True` argument can be used to handle exceptions in the tasks.
- if one of the tasks raises an exception, the exception will be returned in the result list
With `return_exceptions=False` (default):
- if one of the tasks raises an exception, the exception will be raised immediately and the other tasks will be cancelled.

```python
async def badasync(n):
    print(f"Starting badasync with n={n}")
    await asyncio.sleep(n)
    if n == 2:
        raise ValueError("An error occurred in badasync")
    else:
        print(f"Slept asynchronously for {n} seconds")
    print(f"Finished badasync with n={n}")
    return n

async def main():
    tasks = [badasync(i) for i in range(1, 4)]
    result = await asyncio.gather(*tasks, return_exceptions=True)
    one, two, three = result
    return [one, two, three]

# With exception = False => unfinished tasks will be cancelled
# Starting 1,2,3; Finished 1; Finished 3; ValueError
# 
# With exception = True => all tasks will be run to completion
# Starting 1,2,3; Finished 1; Finished 3; ValueError; Finished 2 
```

## Task Groups
Uses a context manager to automatically manage the lifecycle of tasks.
With TaskGroup, the exception handling is similar to `return_exceptions=False` in `gather()`.

```python
async def s(n):
    await asyncio.sleep(n)
    return n

async with asyncio.TaskGroup() as tg:
    t1 = tg.create_task(s(3))
    t2 = tg.create_task(s(2))
    t3 = tg.create_task(s(1))
    # no need to await the tasks, they will be awaited when exiting the context manager
```

# Semaphore
A semaphore is a counter that limits the number of tasks that can access a shared resource or perform a particular action at the same time.
# Lock
Lock will block the execution of the code until the lock is released.

```python
semaphore = asyncio.Semaphore(2)
async def my_coro():
    async with semaphore: # This will only allow 2 coroutines to run at a time
        print('Hello')
        await asyncio.sleep(1)
await asyncio.gather(*(my_coro() for i in range(10))) # only the first 2 will run at the same time
```
