import configparser

# Load the configuration
config = configparser.ConfigParser()
config.read('conf.ini')

# there could be different sections in config file
conf_1 = config['Section 2']

# boolean value in config file (either 0, 1 or True/False)
use_proxy = conf_1.getboolean('use_proxy')

# int and float values, there are 2 ways to get them
threads = int(conf_1['threads'])
multithread = conf_1.getint('threads')

# working with lists
# list of strings only, must be in format "item1,item2,item3" without spaces
servers = conf_1['servers'].split(',')
for item in servers:
    print(item)