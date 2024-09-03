import dotenv
import os

# when installing, use pip install python-dotenv, not dotenv

# using environment variable to hide information
# setup .env file like this

# API_KEY="123456789"

# load .env file from current working directory
dotenv.load_dotenv()

API_Key = os.getenv("API_KEY")
print(API_Key)
# expected result: 123456789

# Sometimes when loading .env that contain other information such as codes, only the environments are loaded and the program will function, but dotenv will log many lines are error, to disable error logging, use this

from contextlib import contextmanager
import sys

@contextmanager
def suppress_stderr():
    with open(os.devnull, "w") as devnull:
        sys.stderr = devnull
        yield

with suppress_stderr():
    dotenv.load_dotenv('')
sys.stderr = sys.__stderr__ # restore logging to stderr