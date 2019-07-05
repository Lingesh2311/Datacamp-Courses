## Visualizing the PCA Transformation

### Dimension Reduction
- More efficient storage and computation
- It helps to remove the noisy features

### Principal Component Analysis
- Step 1
    - Decorrelation 
- Step 2
    - Reduce Dimension

### PCA aligns data with axes
- Rotates the data to be aligned with some axes
- Shifts the data samples so they have 0 mean
- No information is lost
- Consists of the `.fit()` and `.transform()` method

### PCA features are not correlated
- Decorrelation is common in PCA

### Pearson Correlation
- Measure for the correlation between two quantities. 
- Ranges from -1 to 1. (0 means no correlation)

### Principal Components
- Denotes the **direction of variance**. 
- Aligns the principal components with the axes.
- Get the components using the `components_` attribute of the PCA object.
- Each row defines the displacement from the mean

### Intrinsic Dimension
- Sometimes a N-D feature dataset can be **intrinsically** denoted using lesser number of features.
- Intrinsic dimension = number of features needed to approximate the dataset
- What is the most compact representation of samples?
- E.g Versicolor of the Iris dataset has 2 intrinsic dimension

### PCA features are ordered by descending values of Variance
- Instrinsic dimension is the number of PCA features which can capture 90% of the variance
- Plot the variance values using 
`plt.bar(features, pca.explained_variance_)`

### Dimension Reduction
- Represent the same data using less features
- Assume low variance features are "noise" and the latter are "informative".
- Specify how many features to keep using 
`PCA(n_components = 2)`

### Word Frequency arrays
- Rows represent the documents, columns represent the words
- Entries measure the presence of each word in each document
- Lots of zeros using `scipy.sparse.csr_matrix` will help.
- `csr` stands for compressed sparse row matrix. It will only remember the non-zero positions and save memory

### TruncatedSVD and `csr_matrix`
- Scikit-learn doesn't support `csr_matrix` instead use `TruncatedSVD`
