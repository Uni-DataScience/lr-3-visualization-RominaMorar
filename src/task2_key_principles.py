import pandas as pd
import numpy as np
import seaborn as sns
from matplotlib import pyplot as plt

def create_scatter_plot(data):
    """
    Creates a scatter plot using Seaborn and returns the figure.

    Parameters:
    data (DataFrame): A DataFrame containing 'x' and 'y' columns.

    Returns:
    fig: The Matplotlib figure object containing the scatter plot.
    """
    # Set Seaborn styling for better readability
    sns.set_theme(style="whitegrid")
    
    # Create a Matplotlib figure and axes
    fig, ax = plt.subplots(figsize=(8, 6))
    
    # Create the scatter plot
    sns.scatterplot(x='x', y='y', data=data, color='blue', s=50, edgecolor='k', ax=ax)
    
    # Add axis labels and title for clarity
    ax.set_xlabel("Variable X", fontsize=12)
    ax.set_ylabel("Variable Y", fontsize=12)
    ax.set_title("Scatter Plot of X vs Y", fontsize=14)
    
    # Return the figure
    return fig
data = pd.DataFrame({
    'x': np.random.rand(50),  # 50 random values for X
    'y': np.random.rand(50)   # 50 random values for Y
})

# Call the function to create a scatter plot
fig = create_scatter_plot(data)

# Optionally, show the figure (if you want to display it interactively)
plt.show() 