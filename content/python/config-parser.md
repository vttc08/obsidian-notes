### configparser

```python
# Load configuration
import configparser
config = configparser.ConfigParser()
config.read('config.ini')
```

```ini
[DEFAULT]
API_KEY = "ac:5f:de:32:4a:1c"
API_CONCURRENT_USERS = 10
[SERVER]
USE_SSL = True
FORCE_SSL = 0
ALLOWED_PORTS = 8080,8096,4443 # for use in lists
```

```python
# Configs can have multiple sections
DEFAULT = config['DEFAULT']
SERVER = config['SERVER']
```

```python
# Get values of the config
API_KEY = DEFAULT.get('API_KEY',"dont_use_api")
# Getting boolean
USE_SSL = DEFAULT.getboolean('USE_SSL', False)
# user can put 0,1 or True, False
# Getting float or int
PORT = DEFAULT.getint('PORT', 8080)
API_CONCURRENT_USERS = int(DEFAULT.get('API_CONCURRENT_USERS', 10))
```

```python
# Getting list
ALLOWED_PORTS = SERVER.get('ALLOWED_PORTS').split(',')
```

### YAML

```python
import yaml

# Load yaml
with open('config.yaml') as f:
    data = yaml.safe_load(f, Loader=yaml.FullLoader) # loaded as a Python object similar to dict
```

```python
# Get values of the yaml
port = data.get('port', 8080)
IP = data['server']['ip']
```
