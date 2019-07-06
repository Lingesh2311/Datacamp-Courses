## Interpreting Features from Data

### Non-negative Matrix Factorization
- Dimension Reduction technique
- NMF models are interpretable
- East to explain!
- All sample features must be **non-negative** (>=0)

### Interpretable parts
- NMF expresses documents as combinations of topics (or "themes")
- NMF expresses images as combination of patterns

### Usage
`.fit()` and `.transform()` can be used along with `NMF(n_components=2)`
- Works with Numpy array and csr_matrix

### Reconstruction of Samples of Word document frequency
- samples[]: Original Sample frequency of words in document
- `nmf_features() = model.transform()`: Weights corresponding to each component of the reduced dimension.
- `nmf_components() = model.components_`: Reduced dimension components. 
- Apply **M**atrix **F**actorization using the product of the components and the feature values. 

 