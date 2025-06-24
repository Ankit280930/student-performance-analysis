import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the dataset
df = pd.read_csv("StudentsPerformance.csv")

# Show first 5 rows
print("First 5 rows:\n", df.head())

# Show summary statistics
print("\nSummary statistics:\n", df.describe())

# Add average score column
df['average_score'] = (df['math score'] + df['reading score'] + df['writing score']) / 3

# Plot 1: Gender count
sns.countplot(x='gender', data=df)
plt.title('Gender Distribution')
plt.show()

# Plot 2: Average score by gender
sns.barplot(x='gender', y='average_score', data=df)
plt.title('Average Score by Gender')
plt.show()

# Plot 3: Correlation heatmap
sns.heatmap(df.corr(), annot=True, cmap="coolwarm")
plt.title('Correlation Matrix')
plt.show()
