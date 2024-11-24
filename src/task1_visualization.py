import matplotlib.pyplot as plt
import collections
import numpy as np

def plot_distribution(data):
    """
    Plots the distribution of data using a bar chart and returns the figure object.

    Parameters:
    data (array-like): An array of categorical data items.
    
    Returns:
    fig (Figure): A Matplotlib Figure object.
    """
    counter = collections.Counter(data)
    
    categories = list(counter.keys())
    frequencies = list(counter.values())
    
    fig, ax = plt.subplots()
    ax.bar(categories, frequencies, color=['skyblue', 'orange', 'green'])
    
    ax.set_xlabel('Category')
    ax.set_ylabel('Frequency')
    ax.set_title('Frequency Distribution of Categories')
    
    return fig

data = np.random.choice(['A', 'B', 'C'], size=100)

fig = plot_distribution(data)

plt.show()
