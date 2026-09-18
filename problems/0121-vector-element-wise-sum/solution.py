import numpy as np

def vector_sum(a: list[int|float], b: list[int|float]) -> list[int|float]:
	# Return the element-wise sum of vectors 'a' and 'b'.
	# If vectors have different lengths, return -1.

	vsum = -1

	if len(a) == len(b):
		vsum = np.array(a) + np.array(b)


	return vsum
