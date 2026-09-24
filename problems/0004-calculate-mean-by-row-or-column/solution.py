def calculate_matrix_mean(matrix: list[list[float]], mode: str) -> list[float]:
	
	means = []

	if matrix: r, c = len(matrix), len(matrix[0])
	else: return -1

	if mode == 'row':
		for row in range(r):
			mean = 0
			for col in range(c):
				mean += matrix[row][col]

			means.append(mean/c)
	else:
		for col in range(c):
			mean = 0
			for row in range(r):
				mean += matrix[row][col]

			means.append(mean/r)

	
	
	return means