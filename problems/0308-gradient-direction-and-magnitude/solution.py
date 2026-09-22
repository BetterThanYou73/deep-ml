import numpy as np

def gradient_direction_magnitude(gradient: list) -> dict:
	"""
	Calculate the magnitude and direction of a gradient vector.
	
	Args:
		gradient: A list representing the gradient vector
	
	Returns:
		Dictionary containing:
		- magnitude: The L2 norm of the gradient
		- direction: Unit vector in direction of steepest ascent
		- descent_direction: Unit vector in direction of steepest descent
	"""
	# Your code here
	magnitude = np.linalg.norm(gradient)
	direction = np.nan_to_num(np.divide(gradient, magnitude), nan=0.0)
	descent_direction = np.multiply(direction, -1)

	output = {"magnitude": magnitude, "direction": direction, 'descent_direction': descent_direction}

	return output