import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

sales = pd.read_csv('/Users/hp/Desktop/alice/sales_data.csv' ,parse_dates=['Date'])
sales.plot(kind='scatter', x='Customer_Age', y='Revenue', figsize=(6,6))
plt.show()
