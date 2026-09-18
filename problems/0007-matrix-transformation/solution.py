import numpy as np

def transform_matrix(A: list[list[int|float]], T: list[list[int|float]], S: list[list[int|float]]) -> list[list[int|float]]:

	A, T, S = np.array(A), np.array(T), np.array(S)

	if (np.isclose(np.linalg.det(T), 0) or np.isclose(np.linalg.det(S), 0)):
		return -1


	t_inverse = np.linalg.inv(T)
	TAS = t_inverse @ A
	TAS = TAS @ S


	return TAS.tolist()

