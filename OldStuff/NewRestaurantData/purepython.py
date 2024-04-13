import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Read data
df = pd.read_csv('NewRestaurantData/restaurant_sales_data.csv')

# Calculate total sales for each item
#initially i had a very complicated system including lots of for loops for making this work, and chatgpt showed me the built in pandas functions that can do all of that very efficiently. 
#groupby is a fantastic function, which as you can see works by 
item_sales = df.groupby('Item')['Price'].sum()
total_sales = item_sales + df.groupby('Item')['Tip'].sum()
#you can think of the type of thing that pandas creates from this as an array, where the index is the item's name.

# Calculate percentages
percentages = total_sales / total_sales.sum()
# Find highest and lowest sales
#both of these are automatically stored as strings. Pandas is really a fantastic library for data analysis.
#idxmax is pandas' function for finding the max/min in their format. It will return the item's name, corresponding to this max (similar to how argmax returns the corresponding index)
highest_sales = percentages.idxmax()
lowest_sales = percentages.idxmin()

# Sort items by sales percentages
sorted_items = percentages.sort_values(ascending=False)

# Plot data
plt.figure(figsize=(19, 5))
#this is another very useful format for plotting datafrmaes. It automatically goes to plt
sorted_items.plot(kind='bar', color='maroon')
plt.xlabel("Dish")
plt.ylabel("Percentage of Total Sales (including tip)")
plt.title("Dish ranked by sales")
plt.show()
