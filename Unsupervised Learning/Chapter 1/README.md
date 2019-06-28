Chapter 1 contains the scripts and notebooks for **Clustering** in Python.

### Unsupervised Learning
- Finds patterns
- Compressing data is important (Dimensionality Reduction)

### Supervised vs Unsupervised
- Labelled vs unlabelled
- No specific prediction task in mind

### Iris Dataset
- There are 3 species - Setosa, Versicolor, Virginica
- Features- Petal length, petal width, sepal length, sepal width
- Columns are measurements/ features
- Rows are observations/ samples
- 4 Dimensional (number of features)

### K-means Clustering
- Find clusters in sample
- Number of clusters to be specified
- Use `sklearn`

### Plots to use
- Scatter Plots are the best option here.

### Measuring the Clustering Quality
- Method 1
    - When labels and species are given: use `pd.crosstab` to evaluate the quality.
- Method 2
    - When no species information is given, then good clustering must produce **tight clusters**. So, measure the **Inertia** which gives how spread out the clusters are (lower the better). It is the sum of the distance from each sample to the centroid of its cluster. Use `model.inertia_` to evaluate its value.

### Number of Clusters
- Refer to the Elbow plot tutorial [here](https://github.com/Lingesh2311/Python-Basics/blob/master/EDA%20Basic%20Tutorials/K-means%20Elbow%20Method.ipynb)



