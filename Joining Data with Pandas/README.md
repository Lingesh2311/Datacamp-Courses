# Joining Data with Pandas

## Chapter 1 - Data Merging Basics

### Inner Join

We will use the pandas package's `merge()` method. This method takes some parameters as inputs. Typically, we feed in the first table name, second table name and the column to match on as the input.

```python
first_table.merge(second_table, on=common_column)
```

When there are same column names in the two tables you're performing the join on. We can expect a suffix to be added to the columns coming from both the tables. We can give the forced suffix entry using the suffixes parameter.

```python
first_table.merge(second_table, on=common_column, suffixes=('_first', 'second'))
```

### One to Many Relationships

It means that every row in the left table is related to one or more rows in the right table.

### Merging Multiple dataframes

We can use the same pattern here:

Three tables:
```python
df1.merge(df2, on='col') \
   .merge(df3, on='col')
```

Four tables:
```python
df1.merge(df2, on='col') \
   .merge(df3, on='col') \
   .merge(df4, on='col')
```

## Chapter 2 - Merging Tables with Different Join Types

### Left Join

Here we will get all the rows from the left dataframe and only those rows from the right table where the key columns match.

```python
left_table.merge(right_table, on='column_name', how='left')
```

### Other Joins

There is right join, outer join

```python
left_table.merge(right_table, left_on='col_on_left', right_on='col_on_right', how='outer')
```

### Self Join

The usecase of a self join can be thought of how the graphs in Neo4j works.

When merging the table with itself we can specify the `left_on` and the `right_on` attributes while calling the merge() function.

This is used for situations like: Hierarchical relationships, Sequential relationships.

### Merging on Indices

The merge method adjusts to intake any index name or column name. The returned table can thus be a result of merging two different tables based on an index column.

Similarly to merge tables based on multi-index we can pass the list of index column names to the `on` argument in the **merge()** method.

When we are using the left_on and right_on parameters in merge we should specify the `left_index=True` and `right_index=True`.

## Chapter 3 - Advanced Merging and Concatenating

### Filtering Joins

This is to fiter observations fromt table based on whether or not they match an observation in another table.

#### Semi-Join

A semi-join filters the observations from the left table down to those observations that have a match in the right table. This is similar to an inner join, but unlike that only the columns from the left table are shown. Finally no duplicate rows from the left table are returned, even if there is one-to-many relationship.

STEP 1:
```python
genre_tracks = genres.merge(top_tracks, on='gid')
print(genre_tracks.head())
```

STEP 2: 
```python
genres['gid'].isin(genres_tracks['gid'])
```

STEP 3:
```python
genres_tracks = genres.merge(top_tracks, on='gid')
top_genres = genres[genres['gid'].isin(genres_tracks['gid'])]
print(top_genres.head())
```

#### Anti-Join

This will return all the columns of the left table that is excluded from the intersection.

We can find this using the `indicator=True` argument in the **merge** function. This will return the joined table which has a special `_merge` column which gives the value as **both** and **left_only**. This can be used to identify the values from the left table that belong only to the left table.

STEP 1:
```python
genres_tracks = genres.merge(top_tracks, on='gid', how='left', indicator=True)
print(genres_tracks.head())
```

STEP 2:
```python
genres_list = genres_tracks.loc[genres_tracks['_merge']=='left_only', 'gid']
print(genres_list.head())
```

STEP 3:
```python
genres_tracks = genres.merge(top_tracks, on='gid', how='left', indicator=True)
gid_list = genres_tracks.loc[genres_tracks['_merge']=='left_only', 'gid']
non_top_genres = genres[genres['gid'].isin(gid_list)]
```

### Concatenate Dataframes together vertically

Pandas has a `.concat()` method which can be used to concatenate two tables both vertically and horizontally. When `axis=0` its vertical (default) and `axis=1` its horizontal.

`pd.concat([first_table, second_table, third_table])`

We can ignore the index to get the result we need:
`pd.concat([first_table, second_table, third_table], ignore_index=True)`

We can instead add custom keys followed by indices using the keys attribute:
`pd.concat([first_table, second_table, third_table], ignore_index=False, keys=['jan', 'feb', 'mar'])`

We can combine the common columns from two tables using the `join='inner'` setting:
`pd.concat([first_table, second_table], join='inner')`


### Verifying Integrity

We can verify the validity of the merge using the `.merge(validate='one_to_one')` method

We can verify the concatenation using the `.concatenate(verify_integrity=True)` method

## Chapter 4 - Merging Ordered and Time-Series Data

### Using `merge_ordered()`

The default call here is `outer`. the calling function is `pd.merge_ordered(df1, df2)`.

This is used for merging time series data from two tables.
```python
pd.merge_ordered(appl, mcd, on='date', suffixes=('_appl','_mcd'))
```

We can fill the missing data using a technique called forward filling.

### Using `merge_asof()`

### Selecting data with `.query()`

### Reshaping data with `.melt()`
