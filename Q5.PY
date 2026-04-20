import numpy as np

emp_id = np.arange(1, 11)

salary = np.random.randint(20000, 100000, 10)
experience = np.random.randint(1, 20, 10)
department = np.random.choice(['HR', 'IT', 'Sales', 'Finance'], 10)

print("Employee ID:", emp_id)
print("Salary:", salary)
print("Experience:", experience)
print("Department:", department)




import pandas as pd
import numpy as np

df = pd.DataFrame({
    'Salary': [50000, np.nan, 70000, 60000],
    'Experience': [5, 10, np.nan, 8],
    'Department': ['IT', 'HR', 'Sales', 'IT']
})

# Fill missing values
df.fillna(df.mean(numeric_only=True), inplace=True)

# Remove duplicates
df.drop_duplicates(inplace=True)

print(df)






import pandas as pd

df = pd.DataFrame({
    'Department': ['IT', 'HR', 'IT', 'Sales'],
    'Salary': [50000, 60000, 70000, 55000]
})

avg_salary = df.groupby('Department')['Salary'].mean()

print("Average Salary per Department:")
print(avg_salary)




import pandas as pd

df = pd.DataFrame({
    'Salary': [50000, 60000, 70000, 150000, 40000]
})

# Outliers (above average)
outliers = df[df['Salary'] > df['Salary'].mean()]

print("Salary Outliers:")
print(outliers)




import seaborn as sns
import matplotlib.pyplot as plt

salary = [50000, 60000, 70000, 150000, 40000]

sns.boxplot(y=salary)
plt.title("Salary Distribution")
plt.show()







import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.DataFrame({
    'Department': ['IT', 'HR', 'Sales', 'Finance'],
    'Salary': [50000, 60000, 55000, 65000]
})

sns.barplot(x='Department', y='Salary', data=df)
plt.title("Department-wise Salary")
plt.show()





import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.DataFrame({
    'Experience': [2, 5, 10, 8, 3],
    'Salary': [30000, 50000, 80000, 60000, 35000]
})

sns.violinplot(x='Experience', y='Salary', data=df)
plt.title("Experience vs Salary")
plt.show()