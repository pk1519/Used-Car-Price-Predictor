import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Assuming you've already loaded the dataset into a DataFrame named 'car'
# car = pd.read_csv('quikr_car.csv')

# Display the first few rows of the DataFrame to understand its structure
print(car.head())

# Now, let's start visualizing the features
# For example, let's create a pairplot to visualize relationships between numerical features
sns.pairplot(car)
plt.show()

# You can also create histograms of numerical features to see their distributions
car.hist(figsize=(12, 8))
plt.show()

# To visualize relationships between numerical and categorical features, you can use boxplots
plt.figure(figsize=(12, 8))
sns.boxplot(x='Fuel_Type', y='Price', data=car)
plt.show()

# You can explore various combinations and types of visualizations based on your dataset and what insights you're looking for.
