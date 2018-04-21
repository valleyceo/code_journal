# Machine Learning Python Cheatsheet
--
## Tool-kits
```pyhon
from IPython.display import display # Allows the use of display() for DataFrames

```

## Numpy
```pyhon
# handy functions: min, max, sum, shape, median, std

```

## Pandas
```pyhon
# read file
data = pd.read_csv(csv_file)

# get feature column
feature_data = data['feature']

# remove feature
data = data.drop('feature', axis = 1)

```

## Print/Plot
```pyhon
# display on jupyter notebook
%matplotlib inline

# display data
display(data.head(n = 5))


```