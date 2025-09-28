# Find Command TLDR Cheatsheet

Search for files and directories:
```bash
find <path> <options>
```

Find regular files/folders:
```bash
find <path> -type f
find <path> -type d  
```

Find by name (case-insensitive):
```bash
find <path> -iname "<pattern>"
```
Find files larger than 10MB:
```bash
find <path> -size +10M
```
Run a command on each found file:
```bash
find <path> <options> -exec <command> {} \;
```
Examples using `-exec`:
```bash
# Delete found files
find <path> -type f -name "*.log" -exec rm {} \;
```
Move files to another directory
```bash
find <path> -type f -name "*.txt" -exec mv {} /destination/dir/ \;
```
Syntax for -exec
```bash
-exec cmd {} \ # {} the placeholder for file
```