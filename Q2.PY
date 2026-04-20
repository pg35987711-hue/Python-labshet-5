import numpy as np

products = ['Product1', 'Product2', 'Product3', 'Product4', 'Product5']

sales = np.random.randint(1000, 10000, 5)
profit = np.random.randint(200, 3000, 5)

print("Products:", products)
print("Sales:", sales)
print("Profit:", profit)





import pandas as pd
import numpy as np

df = pd.DataFrame({
    'Product': ['A', 'B', 'C', 'D'],
    'Sales': [5000, np.nan, 7000, 6000],
    'Profit': [1200, 1500, np.nan, 1300]
})

# Handle missing values
df.fillna(df.mean(numeric_only=True), inplace=True)

# Remove duplicates
df.drop_duplicates(inplace=True)

print(df)




import pandas as pd

df = pd.DataFrame({
    'Product': ['A', 'B', 'C', 'A'],
    'Sales': [5000, 6000, 7000, 4000]
})

# Total sales per product
total_sales = df.groupby('Product')['Sales'].sum()

# Average sales per product
avg_sales = df.groupby('Product')['Sales'].mean()

print("Total Sales:\n", total_sales)
print("Average Sales:\n", avg_sales)








import pandas as pd

df = pd.DataFrame({
    'Product': ['A', 'B', 'C', 'D'],
    'Sales': [5000, 6000, 7000, 3000]
})

# Best product
best = df[df['Sales'] == df['Sales'].max()]

# Worst product
worst = df[df['Sales'] == df['Sales'].min()]

print("Best Performing Product:")
print(best)

print("Worst Performing Product:")
print(worst)





import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.DataFrame({
    'Product': ['A', 'B', 'C', 'D'],
    'Sales': [5000, 6000, 7000, 3000]
})

sns.barplot(x='Product', y='Sales', data=df)
plt.title("Sales vs Product")
plt.show()




import matplotlib.pyplot as plt

sales = [5000, 6000, 7000, 3000]

plt.plot(sales)
plt.title("Sales Trend")
plt.xlabel("Products")
plt.ylabel("Sales")
plt.show()





import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.DataFrame({
    'Sales': [5000, 6000, 7000, 3000],
    'Profit': [1200, 1500, 2000, 800]
})

sns.heatmap(df.corr(), annot=True)
plt.title("Sales & Profit Correlation")
plt.show()