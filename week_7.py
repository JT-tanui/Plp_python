import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Loading the Iris dataset from seaborn for convenience
iris = sns.load_dataset('iris')

# Display the first few rows of the dataset
print(iris.head())

# Check the data types and missing values
print(iris.info())

# Display basic statistics for numerical columns
print(iris.describe())

# Cleaning the dataset (No missing values in the Iris dataset, but for illustration):
iris_cleaned = iris.dropna()  # Drop rows with missing values
# Alternatively, you can fill missing values
# iris_filled = iris.fillna(iris.mean())

# Grouping by 'species' and calculating the mean for numerical columns
species_mean = iris.groupby('species').mean()
print(species_mean)

# Line plot example: Species vs Sepal Length
plt.figure(figsize=(10, 6))
sns.lineplot(data=iris, x='species', y='sepal_length', marker='o')
plt.title('Sepal Length by Species')
plt.xlabel('Species')
plt.ylabel('Sepal Length (cm)')
plt.grid(True)  # Add gridlines for readability
plt.show()

# Bar plot for average petal length per species
plt.figure(figsize=(10, 6))
sns.barplot(data=iris, x='species', y='petal_length', palette='viridis')
plt.title('Average Petal Length by Species')
plt.xlabel('Species')
plt.ylabel('Petal Length (cm)')
plt.grid(True)  # Add gridlines for readability
plt.show()

# Histogram for sepal length distribution
plt.figure(figsize=(10, 6))
sns.histplot(iris['sepal_length'], bins=15, kde=True, color='blue')
plt.title('Distribution of Sepal Length')
plt.xlabel('Sepal Length (cm)')
plt.ylabel('Frequency')
plt.grid(True)  # Add gridlines for readability
plt.show()

# Scatter plot between sepal length and petal length
plt.figure(figsize=(10, 6))
sns.scatterplot(data=iris, x='sepal_length', y='petal_length', hue='species', style='species', palette='deep')
plt.title('Sepal Length vs Petal Length')
plt.xlabel('Sepal Length (cm)')
plt.ylabel('Petal Length (cm)')
plt.legend(title='Species')
plt.grid(True)  # Add gridlines for readability
plt.show()

# Handling CSV loading with error handling
try:
    # Load a CSV dataset (adjust the file path if needed)
    df = pd.read_csv('dataset.csv')
except FileNotFoundError:
    print("Error: The file was not found.")
except pd.errors.EmptyDataError:
    print("Error: The file is empty.")
except Exception as e:
    print(f"An error occurred: {e}")
