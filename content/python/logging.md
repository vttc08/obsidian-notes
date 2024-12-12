### Python Logging
Overview
Logger is the object of logging, it creates log messages and pass through any filters, then it will pass to individual handlers (file, email, stream). Each handler have levels, filters which also process logs. Each handler has a formatter which formats the log message to text object.

https://docs.python.org/3/library/logging.html#logrecord-attributes

```python
import logging
# Levels of logging from least to most important: DEBUG, INFO, WARNING, ERROR, CRITICAL
# default level is WARNING
```

```python
# Configure logging
logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logging.info('This is a debug message')

```

```python
# fstring also works
name = 'John'
logging.error(f'{name} is now using the script')
```

    ERROR:root:John is now using the script

```python
# Log Exceptions using exc_info=True
try:
    yourlist = mylist[0]
except Exception as e:
    logging.error("An error occurred", exc_info=True)
    logging.exception("Another way to log exceptions")
```

    ERROR:root:Another way to log exceptions
    Traceback (most recent call last):
      File "C:\Users\hubcc\AppData\Local\Temp\ipykernel_29900\2841400632.py", line 3, in <module>
        yourlist = mylist[0]
    NameError: name 'mylist' is not defined. Did you mean: 'list'?

```python
# Custom Loggers
logger = logging.getLogger(__name__) # use a name for each module
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
handler = logging.StreamHandler()
handler.setFormatter(formatter)
logger.addHandler(handler)
logger.debug('This is a debug message')
logger.info('This is an info message')
```

```python
# Logger from another library (useful for different logging levels), eg. httpx less verbose my program more verbose
import httpx
logging.basicConfig(level=logging.INFO) # set default level
httpx_logger = logging.getLogger('httpx')
httpx_logger.setLevel(logging.WARNING) # set level for httpx
logger = logging.getLogger(__name__)
```

    INFO:newlogger:This is an info message

```python
# Logger for other modules
# In module1.py
import logging
logger = logging.getLogger(__name__)
logger.info('Hello from module1')
# In main.py
import logging
import module1
logger = logging.getLogger(__name__)
logger.info('Hello from main')
# Result
```

    INFO:module1:Hello from module1
    INFO:__main__:Hello from main

When importing other modules in Python, everything not in __main__ is executed, including loggers. If the logger from other module is imported before the `logging.basicConfig()` is called, the logger will not be configured properly. However, it's possible to use import another module such as `config.py` before functional modules and configure the logger in `config.py`.

### Putting it together

```python
# main.py
import config
from web import httpxfunc
logger = logging.getLogger(__name__)
logger.info('Hello from main')
mod2.httpxfunc()
```

```python
# config.py
import logging
logging.basicConfig(format="%(asctime)s") # import any other configurations here
```

```python
# web.py
import httpx
import logging
logger = logging.getLogger(__name__)
httpx_logger = logging.getLogger('httpx')
httpx_logger.setLevel(logging.DEBUG) # set level to debug
async def httpxfunc():
    pass # pretend it does something
```

```python
# Results
```

    2024-01-01 00:00:00,000 - main - INFO - Hello from main # already formatted by config.py
    2024-01-01 00:00:00,000 - web - INFO - Hello from web # logging from web.py
    2024-01-01 00:00:00,000 - httpx - DEBUG - load_ssl_context verify=True # Debug also shown from httpx as it's set to DEBUG

