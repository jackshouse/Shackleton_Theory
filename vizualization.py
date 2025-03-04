import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

def plot_geodesic(trajectory):
    """Plots the trajectory of a test particle moving in a curved time geodesic."""
    fig = plt.figure(figsize=(8, 6))
    ax = fig.add_subplot(111, projection='3d')
    
    ax.plot(trajectory[:, 0], trajectory[:, 1], trajectory[:, 2], label='Particle Path', color='blue')
    
    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_zlabel('Z')
    ax.set_title('Simulated Test Particle Motion in Curved Time Geodesic')
    ax.legend()
    
    plt.show()
