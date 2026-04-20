import numpy as np

# Generate data
n = 20

age = np.random.randint(18, 60, n)
income = np.random.randint(20000, 100000, n)
spending_score = np.random.randint(1, 100, n)

print("Age:", age)
print("Income:", income)
print("Spending Score:", spending_score)





import pandas as pd
import numpy as np

n = 20

df = pd.DataFrame({
    'Age': np.random.randint(18, 60, n),
    'Income': np.random.randint(20000, 100000, n),
    'Spending_Score': np.random.randint(1, 100, n)
})

print(df)





import pandas as pd

df = pd.DataFrame({
    'Age': [25, 30, 35, 40],
    'Income': [30000, 50000, 70000, 90000],
    'Spending_Score': [40, 60, 80, 20]
})

print("Mean:\n", df.mean())
print("Median:\n", df.median())
print("Std Dev:\n", df.std())






import pandas as pd

df = pd.DataFrame({
    'Income': [30000, 50000, 70000, 90000],
    'Spending_Score': [40, 60, 80, 20]
})

# Categorization
def category(row):
    if row['Income'] > 60000 and row['Spending_Score'] > 60:
        return 'High Value'
    elif row['Income'] > 60000:
        return 'Rich'
    elif row['Spending_Score'] > 60:
        return 'Big Spender'
    else:
        return 'Normal'

df['Category'] = df.apply(category, axis=1)

print(df)





import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.DataFrame({
    'Income': [30000, 50000, 70000, 90000],
    'Spending_Score': [40, 60, 80, 20],
    'Category': ['Normal', 'Big Spender', 'High Value', 'Rich']
})

sns.scatterplot(x='Income', y='Spending_Score', hue='Category', data=df)
plt.title("Customer Segmentation")
plt.show()




import pandas as pd
import seaborn as sns

df = pd.DataFrame({
    'Age': [25, 30, 35, 40],
    'Income': [30000, 50000, 70000, 90000],
    'Spending_Score': [40, 60, 80, 20]
})

sns.pairplot(df)




import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.DataFrame({
    'Income': [30000, 50000, 70000, 90000, 45000, 80000]
})

sns.boxplot(y='Income', data=df)
plt.title("Income Distribution")
plt.show()