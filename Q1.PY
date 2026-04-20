import numpy as np

# Generate data
students = 10

math_marks = np.random.randint(40, 100, students)
science_marks = np.random.randint(40, 100, students)
english_marks = np.random.randint(40, 100, students)
age = np.random.randint(15, 20, students)

print("Math:", math_marks)
print("Science:", science_marks)
print("English:", english_marks)
print("Age:", age)




import pandas as pd
import numpy as np

students = 10

df = pd.DataFrame({
    'Math': np.random.randint(40, 100, students),
    'Science': np.random.randint(40, 100, students),
    'English': np.random.randint(40, 100, students),
    'Age': np.random.randint(15, 20, students)
})

print(df)




import pandas as pd
import numpy as np

df = pd.DataFrame({
    'Math': [80, 90, np.nan, 70],
    'Science': [85, np.nan, 75, 65],
    'English': [88, 92, 78, np.nan],
    'Age': [16, 17, 16, 17]
})

# Fill missing values
df.fillna(df.mean(numeric_only=True), inplace=True)

# Remove duplicates
df.drop_duplicates(inplace=True)

print(df)







import pandas as pd

df = pd.DataFrame({
    'Math': [80, 90, 70, 60],
    'Science': [85, 75, 65, 70],
    'English': [88, 92, 78, 80]
})

print("Mean:\n", df.mean())
print("Median:\n", df.median())
print("Std Dev:\n", df.std())











import pandas as pd

df = pd.DataFrame({
    'Total_Marks': [270, 250, 200, 180]
})

def grade(marks):
    if marks >= 270:
        return 'A'
    elif marks >= 240:
        return 'B'
    elif marks >= 200:
        return 'C'
    else:
        return 'D'

df['Grade'] = df['Total_Marks'].apply(grade)

print(df)








import matplotlib.pyplot as plt

marks = [80, 90, 70, 60]

plt.plot(marks)
plt.title("Marks Trend")
plt.xlabel("Students")
plt.ylabel("Marks")
plt.show()