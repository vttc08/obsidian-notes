### Working with Pandas

content of the csv file (file.csv) is as follows:
```
name,city,happiness(0-10),height(cm),weight(kg)
John,Kolkata,7,182,72.2
Michael,Delhi,6,168,65.8
David,Mumbai,8,163,59.9
Sarah,Chennai,9,155,52.7
Daniel,Kolkata,7,179,71.1
Emily,Delhi,6,172,66.3
Olivia,Mumbai,8,158,61.7
Ethan,Chennai,9,147,48.9
Sophia,Kolkata,7,183,73.5
Matthew,Delhi,6,169,66.9
Karen,Mumbai,8,161,59.1
James,Chennai,9,152,51.3
Zoe,Kolkata,7,177,70.8
Logan,Delhi,6,173,65.1
Hannah,Mumbai,8,159,61.3
Liam,Chennai,9,148,49.8
Emma,Kolkata,7,181,72.7
Ava,Delhi,6,170,66.1
Noah,Mumbai,8,162,60.3
Mia,Chennai,9,153,52.5
Benjamin,Kolkata,7,178,70.1
Aria,Delhi,6,171,65.5
William,Mumbai,8,160,59.7
Grace,Chennai,9,150,50.1

```

```python
# read csv file
import pandas as pd

df = pd.read_csv('file.csv')
```

```python
# access a column of data
df['city'].head() # head is used to display the first 5 rows
df.tail() # tail is used to display the last 5 rows
```

    0    Kolkata
    1      Delhi
    2     Mumbai
    3    Chennai
    4    Kolkata
    Name: city, dtype: object

```python
# access multiple column of data
df[['name', 'city']].head()
```

<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>name</th>
      <th>city</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>John</td>
      <td>Kolkata</td>
    </tr>
    <tr>
      <th>1</th>
      <td>Michael</td>
      <td>Delhi</td>
    </tr>
    <tr>
      <th>2</th>
      <td>David</td>
      <td>Mumbai</td>
    </tr>
    <tr>
      <th>3</th>
      <td>Sarah</td>
      <td>Chennai</td>
    </tr>
    <tr>
      <th>4</th>
      <td>Daniel</td>
      <td>Kolkata</td>
    </tr>
  </tbody>
</table>
</div>

**iloc vs loc**
- iloc is used to access rows and columns by integer index -eg. 0
- loc is used to access rows and columns by label -eg. city

```python
# access a row of data
df.iloc[0] # access the first row
```

    name                  John
    city               Kolkata
    happiness(0-10)          7
    height(cm)             182
    weight(kg)            72.2
    Name: 0, dtype: object

```python
# Access multiple rows
df.iloc[0:2]  # access the first 5 rows
# row range, column range
```

<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>name</th>
      <th>city</th>
      <th>happiness(0-10)</th>
      <th>height(cm)</th>
      <th>weight(kg)</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>John</td>
      <td>Kolkata</td>
      <td>7</td>
      <td>182</td>
      <td>72.2</td>
    </tr>
    <tr>
      <th>1</th>
      <td>Michael</td>
      <td>Delhi</td>
      <td>6</td>
      <td>168</td>
      <td>65.8</td>
    </tr>
  </tbody>
</table>
</div>

```python
# Access a specific cell
df.loc[0, 'city'] # the city of the first row
```

    'Kolkata'

```python
# Access multiple cells
df.loc[0:2, ['name', 'city']] # the name and city of the first 3 rows
df.loc[:,['name','city']] # the name and city of all rows
```

<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>name</th>
      <th>city</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>John</td>
      <td>Kolkata</td>
    </tr>
    <tr>
      <th>1</th>
      <td>Michael</td>
      <td>Delhi</td>
    </tr>
    <tr>
      <th>2</th>
      <td>David</td>
      <td>Mumbai</td>
    </tr>
  </tbody>
</table>
</div>

```python
# Select rows based on a condition
df[df['height(cm)'] > 155]
df[df['city']=='Kolkata'].head() # select rows where city is Kolkata
df[df['city'].isin(['Kolkata', 'Delhi'])] # select using isin and select all rows where the content of the city column matches a list
```

    (      name     city  happiness(0-10)  height(cm)  weight(kg)
     0     John  Kolkata                7         182        72.2
     1  Michael    Delhi                6         168        65.8
     2    David   Mumbai                8         163        59.9
     4   Daniel  Kolkata                7         179        71.1
     5    Emily    Delhi                6         172        66.3,
           name     city  happiness(0-10)  height(cm)  weight(kg)
     0     John  Kolkata                7         182        72.2
     4   Daniel  Kolkata                7         179        71.1
     8   Sophia  Kolkata                7         183        73.5
     12     Zoe  Kolkata                7         177        70.8
     16    Emma  Kolkata                7         181        72.7)

```python
# select row based on multiple conditions
new_df_3 = df[(df['height(cm)'] >= 155) & (df['height(cm)'] < 175)].head() # selecting a value between 2 numbers is considered as a multiple condition
new_df_4 = df[(df['city']=='Kolkata') | (df['city']=='Mumbai')].head() # using the or operator
new_df_3, new_df_4
```

    (      name     city  happiness(0-10)  height(cm)  weight(kg)
     1  Michael    Delhi                6         168        65.8
     2    David   Mumbai                8         163        59.9
     3    Sarah  Chennai                9         155        52.7
     5    Emily    Delhi                6         172        66.3
     6   Olivia   Mumbai                8         158        61.7,
          name     city  happiness(0-10)  height(cm)  weight(kg)
     0    John  Kolkata                7         182        72.2
     2   David   Mumbai                8         163        59.9
     4  Daniel  Kolkata                7         179        71.1
     6  Olivia   Mumbai                8         158        61.7
     8  Sophia  Kolkata                7         183        73.5)

```python
# get the unique values of a column
df['city'].unique()
```

    array(['Kolkata', 'Delhi', 'Mumbai', 'Chennai'], dtype=object)

```python
# 2d dataframe array can be converted into a python dictionary
dict(df.head())
```

    0       John
    1    Michael
    2      David
    3      Sarah
    4     Daniel
    Name: name, dtype: object

```python
# 1d dataframe array (eg. a column, row) can be converted into a python list or a dictionary
list(df['name'].head()) # column list
list(df.iloc[0]) # row list
dict(df.iloc[0])
```

```python
# Deal with Missing Data
df.dropna(how='any') # drop rows with missing data
df.fillna(value=0) # fill missing data with a specified value
```
