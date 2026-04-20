import numpy as np

# Generate data
products = ['A', 'B', 'C', 'D', 'E']

sales = np.random.randint(1000, 10000, 5)
profit = np.random.randint(200, 3000, 5)

print("Sales:", sales)
print("Profit:", profit)




import pandas as pd
import numpy as np

df = pd.DataFrame({
    'Product': ['A', 'B', 'C', 'D', 'E'],
    'Sales': np.random.randint(1000, 10000, 5),
    'Profit': np.random.randint(200, 3000, 5)
})

print(df)






import pandas as pd
import numpy as np

df = pd.DataFrame({
    'Sales': [5000, np.nan, 7000, 6000],
    'Profit': [1200, 1500, np.nan, 1300]
})

# Fill missing values
df.fillna(df.mean(numeric_only=True), inplace=True)

# Remove duplicates
df.drop_duplicates(inplace=True)

print(df)









import pandas as pd

df = pd.DataFrame({
    'Sales': [5000, 6000, 7000, 8000],
    'Profit': [1200, 1500, 1800, 2000]
})

print("Mean:\n", df.mean())
print("Median:\n", df.median())
print("Std Dev:\n", df.std())






import pandas as pd

df = pd.DataFrame({
    'Sales': [5000, 6000, 7000],
    'Profit': [1200, 1500, 1800]
})

# New feature: Profit Margin
df['Profit_Margin'] = df['Profit'] / df['Sales']

print(df)





import matplotlib.pyplot as plt

sales = [5000, 6000, 7000, 8000]

plt.plot(sales)
plt.title("Sales Trend")
plt.xlabel("Time")
plt.ylabel("Sales")
plt.show()





import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.DataFrame({
    'Product': ['A', 'B', 'C'],
    'Sales': [5000, 6000, 7000]
})

sns.barplot(x='Product', y='Sales', data=df)
plt.title("Product Sales")
plt.show()




import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.DataFrame({
    'Sales': [5000, 6000, 7000],
    'Profit': [1200, 1500, 1800]
})

sns.heatmap(df.corr(), annot=True)
plt.title("Correlation Heatmap")
plt.show()