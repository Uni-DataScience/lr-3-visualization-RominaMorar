import numpy as np
import pandas as pd
import seaborn as sns
from matplotlib import pyplot as plt

def perform_eda(df):
    """
    Performs EDA including descriptive statistics, outlier detection,
    and correlation analysis.

    Parameters:
    df (DataFrame): A DataFrame containing data for EDA.
    """
    
    print("Descriptive Statistics:")
    descriptive_stats = df.describe().transpose()
    print(descriptive_stats)
    
    modes = df.mode().transpose()
    print("\nMode of each column:")
    print(modes)
    
    plt.figure(figsize=(10, 6))
    sns.boxplot(data=df)
    plt.title("Box Plot for Outlier Detection")
    plt.show()
    
    correlation_matrix = df.corr()
    print("\nCorrelation Matrix:")
    print(correlation_matrix)
    
    plt.figure(figsize=(10, 8))
    sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', fmt='.2f', linewidths=0.5)
    plt.title("Correlation Heatmap")
    plt.show()

# Example data
df = pd.DataFrame({
    'A': np.random.rand(50),
    'B': np.random.rand(50) * 10,
    'C': np.random.rand(50) * 100
})
perform_eda(df)
