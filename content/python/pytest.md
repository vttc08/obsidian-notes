## Pytest

```shell
pip install pytest
```

```python
def myfunc(a):
    return a+1
```

```python
# import the function
from .. import myfunc

def test_myfunc():
    assert myfunc(1) == 2 # use assert to 
```

Running the pytest
- first it searches for tests in `tests` folder
- run every function with assert and give output
