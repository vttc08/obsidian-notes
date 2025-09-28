Basic grep
```bash
grep $expression file
```
case insensitive
```bash
grep -i $expression file
```
search for entire word
```bash
grep -w $expression file
```
recursive search (search directory)
```bash
grep -r $expression directory/
```
show lines above and below match (context)
```bash
grep -C 2 $expression file
```
count matches
```bash
grep -c $expression file
```
list files with matches
```bash
grep -l $expression *
```
Perl compatible regex
```bash
grep -P "\d{2}" file
```
