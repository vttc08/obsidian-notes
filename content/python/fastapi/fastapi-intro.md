### FastAPI Fundamentals
```
pip install fastapi uvicorn
```

```python
from fastapi import FastAPI
app = FastAPI()
```

```python
# GET
items = []
@app.get("/items/{item_id}") # uses {item_id} as a parameter
def get_item(item_id: int): # item_id is a parameter and fastapi will convert it to an integer
    return items[item_id]
```

```python
# Path parameters
@app.get("/items")
def read_item(item: str = "default"): # type declaration and default value
    return {"item": item}
# curl -X 'GET' 'http://server/items?item=foo'
```

```python
# HTTP Exception
from fastapi import HTTPException
@app.get("/unauthorized")
def unauthorized():
    raise HTTPException(status_code=401, detail="Unauthorized")
```

```python
# BaseModels
from pydantic import BaseModel
from typing import Optional
class Item(BaseModel):
    name: str # required
    is_done: Optional[bool] = None # = None makes it optional
@app.post("/items/")
def create_item(item: Item): # item now follows the Item model
    return item
# curl -X 'POST' 'http://server/items/' -H 'Content-Type: application/json' -d '{"name": "foo", "is_done": true}' must follow the Item model
```

```python
# Response Model
@app.get("/items/{item_id}", response_model=Item)
def read_item(item_id: int) -> Item:
    return items[item_id]
```

### Pydantic Base Model
The basemodel provide type hinting and validation. 

```python
class Item(BaseModel):
    name: str
    description: Optional[str] = None
    price: float

apple = Item(name="Apple", price=1.5) # create an instance of Item
apple_json = {"name": "Apple", "price": 1.5}
newapple = Item(**apple_json) # unpack json or dict
apple_json = newapple.model_dump() # model_dump or json()
```

```python
# Custom validation
@validator("price") # the validator is in the Item class
def validate_price(cls, value): # class and value
    raise ValueError("Price must be greater than 0") if value <= 0 else value
    return value

```
