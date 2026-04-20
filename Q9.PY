import numpy as np

# Generate data
marks = np.random.randint(40, 100, 20)
category = np.random.choice(['General', 'OBC', 'SC', 'ST'], 20)
status = np.random.choice(['Selected', 'Rejected'], 20)

print("Marks:", marks)
print("Category:", category)
print("Status:", status)




import pandas as pd
import numpy as np

df = pd.DataFrame({
    'Marks': [80, 90, np.nan, 70],
    'Category': ['General', 'OBC', 'SC', 'ST'],
    'Status': ['Selected', 'Rejected', 'Selected', 'Rejected']
})

# Fill missing values
df.fillna(df.mean(numeric_only=True), inplace=True)

# Remove duplicates
df.drop_duplicates(inplace=True)

print(df)





import pandas as pd

df = pd.DataFrame({
    'Status': ['Selected', 'Rejected', 'Selected', 'Selected']
})

selection_ratio = df['Status'].value_counts(normalize=True)

print("Selection Ratio:")
print(selection_ratio)






import pandas as pd

df = pd.DataFrame({
    'Category': ['General', 'OBC', 'SC', 'General'],
    'Marks': [85, 75, 65, 90]
})

avg_marks = df.groupby('Category')['Marks'].mean()

print("Average Marks by Category:")
print(avg_marks)





import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.DataFrame({
    'Status': ['Selected', 'Rejected', 'Selected', 'Rejected', 'Selected']
})

sns.countplot(x='Status', data=df)
plt.title("Admission Status Count")
plt.show()





import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.DataFrame({
    'Category': ['General', 'OBC', 'SC', 'ST'],
    'Selection': [50, 40, 30, 20]
})

sns.barplot(x='Category', y='Selection', data=df)
plt.title("Category vs Selection")
plt.show()





import matplotlib.pyplot as plt
import numpy as np

marks = np.random.randint(40, 100, 20)

plt.hist(marks)
plt.title("Marks Distribution")
plt.xlabel("Marks")
plt.ylabel("Frequency")
plt.show()