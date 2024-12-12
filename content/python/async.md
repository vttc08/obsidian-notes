# Python Async
Event Loop - manage distribute tasks
- when a task await, it will be put into the event loop and another task will run

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

# Tasks
Tasks allow you to run multiple coroutines concurrently (run another coroutine while waiting for the first one to finish)

```python
# Create a task
task = asyncio.create_task(main())
task2 = asyncio.create_task(main())
await task # wait for the task to finish before continuing
# but as soon as task is delayed, task2 can be run
```

```python
# Another way to create tasks is using gather
await asyncio.gather(main(), main(), main())
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

```python
lock = asyncio.Lock()
async def my_coro():
    print("no lock") # no lock will be printed first and immediately
    await asyncio.sleep(3)
    async with lock:
        print('Hello')
        await asyncio.sleep(1)
await asyncio.gather(*(my_coro() for i in range(5))) # 
```

    no lock
    no lock
    no lock
    no lock
    no lock
    Hello
    Hello
    Hello
    Hello
    Hello

    [None, None, None, None, None]

