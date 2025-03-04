import numpy as np

def quantum_fluctuation(scale=0.01):
    """Generates a small quantum fluctuation effect for perturbing time geodesics."""
    return np.random.normal(0, scale, 3)

def apply_quantum_effects(trajectory, fluctuation_scale=0.01):
    """Applies quantum fluctuations to a computed geodesic trajectory."""
    noisy_trajectory = trajectory.copy()
    
    for i in range(len(noisy_trajectory)):
        noisy_trajectory[i] += quantum_fluctuation(scale=fluctuation_scale)
    
    return noisy_trajectory
