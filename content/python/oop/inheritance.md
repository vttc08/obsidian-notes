Python Inheritance

```python
class Animal:
    def __init__(self, name):
        self.name = name
```

```python
class Dog(Animal):
    def __init__(self, name, breed):
        super().__init__(name)
        self.breed = breed
```

The `super()` function is used to call the constructor of the parent class, allowing you to initialize inherited attributes and methods.

```python
mydog = Dog("Name", "Breed")
```

```python
class Cat(Animal):
    def __init__(self, name, color):
        super().__init__(name)
        self.color = color
    
    def meow(self):
        return "Meow!"
```

```python
mycat = Cat("Whiskers", "Tabby")
mycat.meow()
```

    'Meow!'

```python
class Kitten(Cat):
    def __init__(self, name, color, age):
        super().__init__(name, color)
        self.age = age
    
    def purr(self):
        return "Purr!"
```

```python
kitty = Kitten("Fluffy", "White", 1)
kitty.meow(); kitty.purr()
```

    'Purr!'

