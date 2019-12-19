![](https://imgur.com/UTsF4ji.png)


ROI - Return on Investment is an all inclusive python package for maketing analytics. The first release focuses on cohort analysis.
The plan is to slowly include more analysis, as the package grows. 

### Installation:
---
You can install **ROI** using 

```
pip install roi
```

### Usage:
---
Example: Cohort Analysis 
```python
import pandas as pd
import matplotlib.pyplot as plt
from roi import cohort analysis

# Read dataset 
data= pd.read_csv('/content/data.csv',encoding='latin',parse_dates=['OrderDate'])

#Pass the dataframe to an instance of cohort analysis class and along with column name of UserId and ActivityDate.
analysis = cohort_analysis(input_df=data, ActivityDate='OrderDate', CustomerID='UserId')

## Generate retention heatmap

analysis.plot_retention()



```


![](https://imgur.com/XVM3TkC.png)
