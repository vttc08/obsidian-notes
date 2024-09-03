import os
import shutil
import sys

# Basic Operation
shutil.move("source", "target") # move the file from readfile to writefile
shutil.copy("source", "target") # copy the file from readfile to writefile
shutil.copytree("source", "target") # copy the directory from source to target, similar to cp -r
os.remove("writefile.txt") # remove the file
os.rmdir("source") # remove the directory
os.mkdir("source") # make the directory
os.chdir("/path/of/this/project") # change directory to source
os.getenv("HOME") # get the environment variable
os.link("source", "target") # create a hard link

# In Windows to give a absolute path with backlashes, use r"string" or double backlashes
r"C:\Users\user\Documents\Python\python-notes\writefile.txt"
"C:\\Users\\user\\Documents\\Python\\python-notes\\writefile.txt"

# Check if the file exists
os.path.exists('writefile.txt') # if the file exists
os.path.isfile('writefile.txt') # if it's a file
os.path.isdir('writefile.txt') # if it's a directory

# Linux Permissions
os.chmod("writefile.txt", 0o777) # must add 0o to the permission number
os.chown("writefile.txt", 1000, 1000) # change ownership by uid and gid

# Path
os.path.realpath("writefile.txt") # get the full path of the file or current directory if no arguments given
os.path.basename("file or dir") # get the file or directory name
'''
r'C:\Users\user\Documents\Python\python-notes\writefile.txt' > 'writefile.txt'
r'C:\Users\user\Documents\Python\python-notes' > 'python-notes'
'''
os.path.dirname("") # get the full directory name
''' r'C:\Users\user\Documents\Python\python-notes' > 'C:\Users\user\Documents\Python'
'''
name, ext = os.path.splitext("writefile.txt") # writefile, .txt
os.path.expanduser("~") # get the full path of the user directory > /home/user

# ls
os.listdir('') # get all files and directory in a folder as a list
for root, dirnames, filenames in os.walk(''):
    print(root, dirnames, filenames)
'''
os.walk('.') return a generator > ('.', ['dir1', 'dir2'], ['file1', 'file2']) ('./dir1', [], ['file3', 'file4'])
root > current directory
dirnames > list of directories in that directory
filenames > list of files in dirname
it will iterate through all the directories
'''
