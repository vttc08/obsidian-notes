Python Dataclasses
================
----------------
Python's `dataclasses` module, introduced in Python 3.7, provides a decorator and functions for automatically adding special methods to user-defined classes. This is particularly useful for classes that are primarily used to store data, as it reduces boilerplate code.

```python
from dataclasses import dataclass, field
```

```python
@dataclass
class MyDataClass:
    x: int
    y: int = 0 # default value, optional
```

The dataclass will provide `__init__`, `__repr__`, and `__eq__` methods automatically based on the class attributes.

With `field`, it allows for more customization of individual fields, such as setting default values, excluding fields from certain methods, and specifying metadata.
Additional field options
- `init=False`: Exclude the field from the generated `__init__` method

```python
@dataclass
class Item:
    name: str
    price: float
    uuid: str = field(default_factory=lambda: str(uuid.uuid4()), repr=False)

# default factory provide a function to generate default values
# repr = False means it will be excluded when printing the object
```

Making a list with dataclass is different

```python
@dataclass
class Objects:
    items: list[Item] = field(default_factory=list)
```
