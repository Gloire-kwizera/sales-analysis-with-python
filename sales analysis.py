import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

sales = pd.read_csv('/Users/hp/Desktop/alice/sales_data.csv' ,parse_dates=['Date'])
sales['Age_Group'].value_counts().plot(kind='pie', figsize=(6,6))
plt.show()
