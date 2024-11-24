import numpy as np
import pandas as pd
import plotly.express as px

def create_interactive_plotly(df):
    """
    Creates an interactive scatter plot using Plotly.

    Parameters:
    df (DataFrame): A DataFrame containing 'x' and 'y' columns.
    
    Returns:
    fig: A Plotly figure object with an interactive scatter plot.
    """
    fig = px.scatter(df, x='x', y='y', 
                     title="Interactive Scatter Plot",
                     labels={'x': 'X Axis', 'y': 'Y Axis'},
                     template='plotly_dark') 
    
    fig.show()
    return fig

# Example data
df = pd.DataFrame({'x': np.random.rand(50), 'y': np.random.rand(50)})
create_interactive_plotly(df)
