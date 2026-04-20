import numpy as np
import pandas as pd

# Generate dates
dates = pd.date_range(start="2023-01-01", periods=30)

# Generate data
cases = np.random.randint(100, 1000, 30)
recoveries = np.random.randint(50, 900, 30)
deaths = np.random.randint(1, 50, 30)

print("Dates:", dates)
print("Cases:", cases)






import pandas as pd
import numpy as np

df = pd.DataFrame({
    'Date': pd.date_range(start="2023-01-01", periods=10),
    'Cases': [500, 600, np.nan, 700, 800, 600, 500, np.nan, 900, 1000],
    'Recoveries': [450, 550, 500, 650, np.nan, 580, 490, 520, 850, 900],
    'Deaths': [10, 15, 12, 18, 20, np.nan, 9, 11, 25, 30]
})

# Fill missing values
df.fillna(df.mean(numeric_only=True), inplace=True)

# Remove duplicates
df.drop_duplicates(inplace=True)

print(df)






import pandas as pd

df = pd.DataFrame({
    'Cases': [500, 600, 700, 800]
})

# Growth rate
df['Growth_Rate'] = df['Cases'].pct_change() * 100

print(df)





import pandas as pd

df = pd.DataFrame({
    'Cases': [500, 600, 700, 800],
    'Recoveries': [450, 550, 600, 750],
    'Deaths': [10, 15, 12, 18]
})

print("Average Cases:", df['Cases'].mean())
print("Max Cases:", df['Cases'].max())

print(df)







import matplotlib.pyplot as plt

cases = [500, 600, 700, 800]

plt.plot(cases)
plt.title("COVID Cases Trend")
plt.xlabel("Days")
plt.ylabel("Cases")
plt.show()





import matplotlib.pyplot as plt

cases = [500, 600, 700, 800, 750, 650]

plt.hist(cases)
plt.title("Cases Distribution")
plt.xlabel("Cases")
plt.ylabel("Frequency")
plt.show()





import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.DataFrame({
    'Cases': [500, 600, 700, 800],
    'Recoveries': [450, 550, 600, 750],
    'Deaths': [10, 15, 12, 18]
})

sns.heatmap(df.corr(), annot=True)
plt.title("COVID Correlation Matrix")
plt.show()