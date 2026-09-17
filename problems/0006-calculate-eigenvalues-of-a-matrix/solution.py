import torch

def calculate_eigenvalues(matrix: torch.Tensor) -> torch.Tensor:
    """
    Compute eigenvalues of a 2x2 matrix using PyTorch.
    Input: 2x2 tensor; Output: 1-D tensor with the two eigenvalues in descending order (highest to lowest).
    """
    # Your implementation here

    imag_eigvals = torch.linalg.eigvals(matrix)

    
    real_eigvals = torch.round(imag_eigvals.real).to(torch.int)

	eigenvalues, _ = torch.sort(real_eigvals, descending=True)

	return eigenvalues