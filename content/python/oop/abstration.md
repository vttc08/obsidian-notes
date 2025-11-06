Python Abstraction using ABC Module

```python
from abc import ABC, abstractmethod
from dataclasses import dataclass
```

```python
@dataclass
class Computer(ABC):
    ram: str
    hdd: str

    @abstractmethod
    def config(self):
        pass
```

```python
@dataclass
class Laptop(Computer):
    battery: str
    plugged: bool = False
    def __post_init__(self):
        super().__init__(self.ram, self.hdd)
    def config(self):
        print(f"Laptop with RAM: {self.ram}, HDD: {self.hdd}, and Battery: {self.battery}")
    def plug_in(self):
        if self.plugged:
            print("Laptop is already plugged in.")
            return
        self.plugged = True
        print("Laptop is plugged in.")
    def unplug(self):
        if not self.plugged:
            print("Laptop is already unplugged.")
            return
        self.plugged = False
        print("Laptop is unplugged.")
```

The `abstraction()` function used, for any classes to inherit from it must implement the abstract methods defined in the base class. 

```python
dell = Laptop("16GB", "1TB", "4000mAh")
dell.config()
dell.plug_in()
dell.unplug()
```

    Laptop with RAM: 16GB, HDD: 1TB, and Battery: 4000mAh
    Laptop is plugged in.
    Laptop is unplugged.

