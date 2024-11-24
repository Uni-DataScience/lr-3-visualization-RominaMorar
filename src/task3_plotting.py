import numpy as np
from matplotlib import pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

def plot_1d(data):
    plt.figure(figsize=(8, 6))
    plt.plot(data, label='1D Line Plot', color='b')
    plt.xlabel('Index')
    plt.ylabel('Value')
    plt.title('1D Data Visualization')
    plt.legend()
    plt.show()

def plot_2d(x, y):
    plt.figure(figsize=(8, 6))
    plt.scatter(x, y, c='r', label='2D Scatter Plot')
    plt.xlabel('X-axis')
    plt.ylabel('Y-axis')
    plt.title('2D Data Visualization')
    plt.legend()
    plt.show()

def plot_3d(x, y, z):
    fig = plt.figure(figsize=(8, 6))
    ax = fig.add_subplot(111, projection='3d')
    ax.scatter(x, y, z, c='g', label='3D Scatter Plot')
    ax.set_xlabel('X-axis')
    ax.set_ylabel('Y-axis')
    ax.set_zlabel('Z-axis')
    ax.set_title('3D Data Visualization')
    ax.legend()
    plt.show()

x = np.linspace(0, 10, 100)
y = np.sin(x)
z = np.cos(x)

plot_1d(x)
plot_2d(x, y)
plot_3d(x, y, z)
