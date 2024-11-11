### Working with Pandas

content of the csv file (file.csv) is as follows:
```
name,city,happiness(0-10),height(cm),weight(kg)
John,Kolkata,7,180,70.45
Michael,Delhi,6,170,67.45
David,Mumbai,8,160,60.45
Sarah,Chennai,9,150,50.45
Daniel,Kolkata,7,180,70.45
Emily,Delhi,6,170,67.45
Olivia,Mumbai,8,160,60.45
Ethan,Chennai,9,150,50.45
Sophia,Kolkata,7,180,70.45
Matthew,Delhi,6,170,67.45
Karen,Mumbai,8,160,60.45
James,Chennai,9,150,50.45
Zoe,Kolkata,7,180,70.45
Logan,Delhi,6,170,67.45
Hannah,Mumbai,8,160,60.45
Liam,Chennai,9,150,50.45
Emma,Kolkata,7,180,70.45
Ava,Delhi,6,170,67.45
Noah,Mumbai,8,160,60.45
Mia,Chennai,9,150,50.45
Benjamin,Kolkata,7,180,70.45
Aria,Delhi,6,170,67.45
William,Mumbai,8,160,60.45
Grace,Chennai,9,150,50.45
```

```python
# read csv file
import pandas as pd

df = pd.read_csv('file.csv')
```

```python
# describe the data
df.describe() # this will describe statistic of all columns with numeric data
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
      <th>happiness(0-10)</th>
      <th>height(cm)</th>
      <th>weight(kg)</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>count</th>
      <td>24.00000</td>
      <td>24.000000</td>
      <td>24.000000</td>
    </tr>
    <tr>
      <th>mean</th>
      <td>7.50000</td>
      <td>165.458333</td>
      <td>62.225000</td>
    </tr>
    <tr>
      <th>std</th>
      <td>1.14208</td>
      <td>11.348163</td>
      <td>7.928773</td>
    </tr>
    <tr>
      <th>min</th>
      <td>6.00000</td>
      <td>147.000000</td>
      <td>48.900000</td>
    </tr>
    <tr>
      <th>25%</th>
      <td>6.75000</td>
      <td>157.250000</td>
      <td>57.500000</td>
    </tr>
    <tr>
      <th>50%</th>
      <td>7.50000</td>
      <td>165.500000</td>
      <td>63.400000</td>
    </tr>
    <tr>
      <th>75%</th>
      <td>8.25000</td>
      <td>174.000000</td>
      <td>67.700000</td>
    </tr>
    <tr>
      <th>max</th>
      <td>9.00000</td>
      <td>183.000000</td>
      <td>73.500000</td>
    </tr>
  </tbody>
</table>
</div>

```python
result = df.describe()
dict(result)['happiness(0-10)']['std'] # descriptive statistics of columns can be converted as a dict to access its values
# better way to access the mean, stdev of a column
df['happiness(0-10)'].mean()
```

    7.5

```python
df['happiness(0-10)'].mean()
df['happiness(0-10)'].std()
df['happiness(0-10)'].median()
df['happiness(0-10)'].quantile(0.25) # 25th percentile
df['city'].mode() # return most frequent values as a list, use mode()[0] to most common value of dataset
# min, max, sum, mean, median, std, var, quantile, mode
```

    0    Chennai
    1      Delhi
    2    Kolkata
    3     Mumbai
    Name: city, dtype: object

## Some Examples

```python
# get average height of people living in both Mumbai and Kolkata
df[(df['city'] == 'Mumbai') | (df['city'] == 'Kolkata')]['height(cm)'].mean()
```

    170.25

```python
# the average height of people living in Chennai with weight above 64kg in 2 decimal places
df[(df['city'] == 'Chennai') & (df['weight(kg)'] < 64)]['height(cm)'].mean().round(2)
```

    150.83

```python
# get the mean and stdev of happiness of people living in Mumbai
df[df['city'] == 'Mumbai']['happiness(0-10)'].mean(), df[df['city'] == 'Mumbai']['happiness(0-10)'].std()
```

    (8.0, 0.0)

