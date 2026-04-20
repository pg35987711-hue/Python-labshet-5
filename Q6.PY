import numpy as np

# Generate stock prices for 30 days
prices = np.random.randint(100, 500, 30)

print("Stock Prices:", prices)




import pandas as pd
import numpy as np

prices = np.random.randint(100, 500, 30)

df = pd.DataFrame({
    'Day': range(1, 31),
    'Price': prices
})




import pandas as pd

df = pd.DataFrame({
    'Price': [100, 120, 130, 150, 170, 160]
})

# Moving Average (3-day)
df['Moving_Avg'] = df['Price'].rolling(window=3).mean()

print(df)




import pandas as pd

df = pd.DataFrame({
    'Price': [100, 120, 130, 150, 170, 160]
})

print("Average Price:", df['Price'].mean())
print("Max Price:", df['Price'].max())

print(df)







import matplotlib.pyplot as plt

prices = [100, 120, 130, 150, 170, 160]

plt.plot(prices)
plt.title("Stock Price Trend")
plt.xlabel("Days")
plt.ylabel("Price")
plt.show()







import matplotlib.pyplot as plt

prices = [100, 120, 130, 150, 170, 160]

plt.hist(prices)
plt.title("Price Distribution")
plt.xlabel("Price")
plt.ylabel("Frequency")
plt.show()






import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.DataFrame({
    'Day': [1, 2, 3, 4],
    'Stock_A': [100, 120, 130, 150],
    'Stock_B': [90, 110, 125, 140]
})

sns.lineplot(x='Day', y='Stock_A', data=df, label='Stock A')
sns.lineplot(x='Day', y='Stock_B', data=df, label='Stock B')

plt.title("Multiple Stock Trends")
plt.show()