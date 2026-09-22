import numpy as np

def linear_regression_gradient_descent(X: np.ndarray, y: np.ndarray, alpha: float, iterations: int) -> np.ndarray:
    """
    Perform linear regression using gradient descent.

    Args:
        X: Feature matrix of shape (m, n) where first column is all ones (for intercept)
        y: Target vector of shape (m,)
        alpha: Learning rate
        iterations: Number of gradient descent iterations
    
    Returns:
        Learned weights as a 1D array of shape (n,)
    """
    m, n = X.shape
    y = y.reshape(-1, 1)  # Ensure y is a column vector
    theta = np.zeros((n, 1))  # Initialize weights to zeros

    # Your code here: implement gradient descent
    for _ in range(iterations):

        # finding out y_pred X @ Theta
        y_pred = np.matmul(X, theta)
        # Loss is defined as y_pred - y_true
        error  = np.subtract(y_pred, y)

        # calculating the gradient 
        grad = np.multiply(np.matmul(np.transpose(X), error), 1/m)

        # updating weights
        theta = np.subtract(theta, np.multiply(grad, alpha))

    return theta.flatten()