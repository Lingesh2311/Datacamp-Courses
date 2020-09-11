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

### Merging on Indices

## Chapter 3 - Advanced Merging and Concatenating

### Filtering Joins

### Concatenate Dataframes together vertically

### Verifying Integrity

## Chapter 4 - Merging Ordered and Time-Series Data

### Using `merge_ordered()`

### Using `merge_asof()`

### Selecting data with `.query()`

### Reshaping data with `.melt()`
