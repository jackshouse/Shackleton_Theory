import numpy as np

def gravitational_potential(x, y, z, M=10):
    """Computes the gravitational potential affecting time curvature."""
    r = np.sqrt(x**2 + y**2 + z**2)
    return -M / (r + 1e-5)  # Avoid singularity

def compute_time_geodesic(initial_position, velocity, steps=100):
    """Computes the path of a test particle in a curved time geodesic."""
    position = np.array(initial_position, dtype=np.float64)
    trajectory = [position.copy()]
    
    for _ in range(steps):
        curvature_effect = gravitational_potential(*position)
        position += velocity * (1 + curvature_effect)  # Modify velocity based on time curvature
        trajectory.append(position.copy())
    
    return np.array(trajectory)
