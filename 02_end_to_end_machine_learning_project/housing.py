# %%
import pandas as pd
import os

csv_path = os.path.join('../', 'datasets', 'housing', 'housing.csv')
housing = pd.read_csv(csv_path)
housing.head()

# %%
housing.info()

# %%
housing["ocean_proximity"].value_counts()

# %%
housing.describe()

# %%
