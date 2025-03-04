import numpy as np
import matplotlib.pyplot as plt
from geodesics import compute_time_geodesic
from visualization import plot_geodesic

# Simulation Parameters
initial_position = [5, 5, 5]  # Starting coordinates in spacetime
initial_velocity = [-0.1, -0.1, -0.1]  # Initial velocity vector
num_steps = 100  # Number of time steps

def run_simulation():
    """Runs the Shackleton Theory time geodesic simulation."""
    trajectory = compute_time_geodesic(initial_position, initial_velocity, num_steps)
    plot_geodesic(trajectory)

if __name__ == "__main__":
    run_simulation()
