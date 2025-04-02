
import matplotlib.pyplot as plt
from sklearn.datasets import load_iris
import pandas as pd

# Load the Iris dataset
iris = load_iris()
iris_df = pd.DataFrame(data=iris.data, columns=iris.feature_names)
iris_df['species'] = iris.target
iris_df['species'] = iris_df['species'].map({0: 'setosa', 1: 'versicolor', 2: 'virginica'})

# Define the color theme
colors = {'setosa': '#8B4513', 'versicolor': '#228B22', 'virginica': '#D2B48C'}  # Brown, Green, Tan

# Visualization 1: Scatter Plot of Petal Length vs. Petal Width
plt.figure(figsize=(8, 6))

# Filter data by species
setosa = iris_df[iris_df['species'] == 'setosa']
versicolor = iris_df[iris_df['species'] == 'versicolor']
virginica = iris_df[iris_df['species'] == 'virginica']

# Plot each species with different colors
plt.scatter(setosa['petal length (cm)'], setosa['petal width (cm)'], color=colors['setosa'], label='Setosa', alpha=0.7)
plt.scatter(versicolor['petal length (cm)'], versicolor['petal width (cm)'], color=colors['versicolor'], label='Versicolor', alpha=0.7)
plt.scatter(virginica['petal length (cm)'], virginica['petal width (cm)'], color=colors['virginica'], label='Virginica', alpha=0.7)

# Add title and labels
plt.title('Petal Length vs. Petal Width', fontsize=16)
plt.xlabel('Petal Length (cm)', fontsize=12)
plt.ylabel('Petal Width (cm)', fontsize=12)

# Add legend
plt.legend(title='Species', fontsize=10)

# Add grid for better readability
plt.grid(True, linestyle='--', alpha=0.5)

# Show the plot
plt.tight_layout()
plt.show()

# Visualization 2: Box Plot of Sepal Length by Species with Median Values
plt.figure(figsize=(8, 6))

# Prepare data for each species
setosa_sepal_length = iris_df[iris_df['species'] == 'setosa']['sepal length (cm)']
versicolor_sepal_length = iris_df[iris_df['species'] == 'versicolor']['sepal length (cm)']
virginica_sepal_length = iris_df[iris_df['species'] == 'virginica']['sepal length (cm)']

# Create the box plot
box_plot = plt.boxplot(
    [setosa_sepal_length, versicolor_sepal_length, virginica_sepal_length],
    labels=['Setosa', 'Versicolor', 'Virginica'],
    patch_artist=True,  # Enable custom box colors
    boxprops=dict(color='black'),  # Box border color
    medianprops=dict(color='red', linewidth=2),  # Median line color
    whiskerprops=dict(color='black'),  # Whisker color
    capprops=dict(color='black')  # Cap color
)

# Apply the color theme to each box
for patch, color in zip(box_plot['boxes'], [colors['setosa'], colors['versicolor'], colors['virginica']]):
    # Set the face color of the box
    patch.set_facecolor(color)
    

# Add median values on the plot
medians = [
    setosa_sepal_length.median(),
    versicolor_sepal_length.median(),
    virginica_sepal_length.median()
]
for i, median in enumerate(medians):
    # Add text for median values
    plt.text(i + 1, median + 0.05, f"{median:.2f}", ha='center', fontsize=10, color='black')

# Add title and labels
plt.title('Sepal Length by Species', fontsize=16)
plt.xlabel('Species', fontsize=12)
plt.ylabel('Sepal Length (cm)', fontsize=12)

# Add grid for better readability
plt.grid(axis='y', linestyle='--', alpha=0.7)

# Show the plot
plt.tight_layout()
plt.show()

# Visualization 3: Overlapping Histograms of Sepal Length by Species
plt.figure(figsize=(10, 6))

# Plot histograms for each species
plt.hist(setosa['sepal length (cm)'], bins=10, alpha=0.7, label='Setosa', color=colors['setosa'], edgecolor='black')
plt.hist(versicolor['sepal length (cm)'], bins=10, alpha=0.7, label='Versicolor', color=colors['versicolor'], edgecolor='black')
plt.hist(virginica['sepal length (cm)'], bins=10, alpha=0.7, label='Virginica', color=colors['virginica'], edgecolor='black')

# Add title and labels
plt.title('Distribution of Sepal Length by Species', fontsize=16)
plt.xlabel('Sepal Length (cm)', fontsize=12)
plt.ylabel('Frequency', fontsize=12)

# Add legend
plt.legend(title='Species', fontsize=10)

# Add grid for better readability
plt.grid(axis='y', linestyle='--', alpha=0.7)

# Show the plot
plt.tight_layout()
plt.show()