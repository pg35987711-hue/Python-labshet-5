import numpy as np

order_id = np.arange(1, 11)

products = np.random.choice(['Laptop', 'Mobile', 'Tablet', 'Headphones'], 10)
quantity = np.random.randint(1, 5, 10)
price = np.random.randint(500, 50000, 10)

print("Order ID:", order_id)
print("Product:", products)
print("Quantity:", quantity)
print("Price:", price)





import pandas as pd

df = pd.DataFrame({
    'Product': ['Laptop', 'Mobile', 'Tablet'],
    'Quantity': [2, 3, 1],
    'Price': [50000, 20000, 15000]
})

# Revenue = Quantity × Price
df['Revenue'] = df['Quantity'] * df['Price']

total_revenue = df['Revenue'].sum()

print("Total Revenue:", total_revenue)
print(df)






import pandas as pd

df = pd.DataFrame({
    'Product': ['Laptop', 'Mobile', 'Tablet', 'Laptop'],
    'Quantity': [2, 3, 1, 4]
})

top_product = df.groupby('Product')['Quantity'].sum().idxmax()

print("Top Selling Product:", top_product)







import pandas as pd
import numpy as np

df = pd.DataFrame({
    'Quantity': [2, np.nan, 3, 4],
    'Price': [50000, 20000, np.nan, 15000]
})

# Fill missing values
df.fillna(df.mean(numeric_only=True), inplace=True)

# Remove duplicates
df.drop_duplicates(inplace=True)

print(df)





import pandas as pd
import matplotlib.pyplot as plt

df = pd.DataFrame({
    'Product': ['Laptop', 'Mobile', 'Tablet'],
    'Sales': [100000, 60000, 15000]
})

plt.bar(df['Product'], df['Sales'])
plt.title("Product Sales")
plt.xlabel("Product")
plt.ylabel("Sales")
plt.show()




import matplotlib.pyplot as plt

products = ['Laptop', 'Mobile', 'Tablet']
sales = [100000, 60000, 15000]

plt.pie(sales, labels=products, autopct='%1.1f%%')
plt.title("Product Distribution")
plt.show()




import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.DataFrame({
    'Quantity': [2, 3, 4],
    'Price': [50000, 20000, 15000],
    'Revenue': [100000, 60000, 60000]
})

sns.heatmap(df.corr(), annot=True)
plt.title("Correlation Heatmap")
plt.show()