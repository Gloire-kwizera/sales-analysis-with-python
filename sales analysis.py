import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

plt.show()
sales = pd.read_csv('/Users/hp/Desktop/alice/sales_data.csv' ,parse_dates=['Date'])
print(sales['Unit_Cost'].describe())