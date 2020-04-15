# -*- coding: utf-8 -*-
import matplotlib.pyplot as plt
import pickle

# Load our data (rb means read binary data)
with open('fruit-sales.pickle', 'rb') as f:
    data = pickle.load(f)
    
# Splitting a list of tuples into two lists
fruit, num_sold = zip(*data)

# Tell matplotlib where to draw the bars
bar_coords = range(len(fruit))
plt.bar(bar_coords, num_sold)

# Replace the x coords with the fruit names
plt.xticks(bar_coords, fruit)

# Add labels and Title
plt.xlabel('Types of Fruit')
plt.ylabel('Number of Fruit (millions)')
plt.title('Number of Fruits Sold (2017)')

# Draw the chart
plt.show