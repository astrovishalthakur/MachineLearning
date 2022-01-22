# Here I show different techniques to handle missing data.

### 1. Complete case Analysis
Complete case anaylsis(CCA), also called "list-wise deletion" of cases, consists in discarding obsercations where vlaues in any of the variables are missing.
Complete Case Analysis means literally analyzing only those observations for which there is information in all of the variabels in the dataset.

### 2. Mean Median Value Imputation
It is used on numerical data, where we fill the missing data with mean or median of available data.

### 3. Arbitrary Value Imputation
Here we fill the missing values with arbitrary values.

### 4. Random Value Imputation
This selects random value from data itself to fill the missing values. Good thing is that it doesn't disturb data distribution to much. But it can affect the covariance in data.

### 5. Missing Value Indicator
It creates a new column which have indicator (0/1, True/False) to tell wheter a column has missing data or not. It seems that it is beneficial if model learns to distinguish between data which has values missing from data which doesn't.

### 6. Automatic Imputation
It is basically doing GridSearchCV to find best imputation techniques with different Hyperparameters.

### 7. KNNImputer
It works on k nearest neighbours algorithm to determine missing value based on other values near to it.

### 8. Iterative Imputer
It's kind of long and based on repetition.
