import numpy as np

# Generate data
temperature = np.random.randint(10, 45, 20)
humidity = np.random.randint(30, 100, 20)
wind_speed = np.random.randint(1, 20, 20)

print("Temperature:", temperature)
print("Humidity:", humidity)
print("Wind Speed:", wind_speed)




import pandas as pd

df = pd.DataFrame({
    'Temperature': [25, 30, 35, 40],
    'Humidity': [60, 70, 80, 90],
    'Wind_Speed': [5, 10, 15, 20]
})

print("Mean:\n", df.mean())
print("Median:\n", df.median())
print("Std Dev:\n", df.std())







import pandas as pd

df = pd.DataFrame({
    'Temperature': [25, 30, 35, 45, 15],
})

# Extreme values (above average)
extreme = df[df['Temperature'] > df['Temperature'].mean()]

print("Extreme Temperature Values:")
print(extreme)






import matplotlib.pyplot as plt

temperature = [25, 30, 35, 40, 28]

plt.plot(temperature)
plt.title("Temperature Variation")
plt.xlabel("Days")
plt.ylabel("Temperature")
plt.show()





import matplotlib.pyplot as plt

temperature = [25, 30, 35, 40]
humidity = [60, 70, 80, 90]

plt.scatter(temperature, humidity)
plt.title("Humidity vs Temperature")
plt.xlabel("Temperature")
plt.ylabel("Humidity")
plt.show()








import seaborn as sns
import matplotlib.pyplot as plt

temperature = [25, 30, 35, 45, 15, 28]

sns.boxplot(y=temperature)
plt.title("Temperature Distribution")
plt.show()