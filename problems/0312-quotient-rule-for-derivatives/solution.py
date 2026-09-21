import numpy as np

def quotient_rule_derivative(g_coeffs: list, h_coeffs: list, x: float) -> float:
    """
    Compute the derivative of f(x) = g(x)/h(x) at point x using the quotient rule.
    
    Args:
        g_coeffs: Coefficients of numerator polynomial in descending order
        h_coeffs: Coefficients of denominator polynomial in descending order
        x: Point at which to evaluate the derivative
        
    Returns:
        The derivative value f'(x)
    """
    # Your code here
    fx = 0

    gx = np.polyval(g_coeffs, x)
    hx = np.polyval(h_coeffs, x)

    numerator = np.polyval(np.polyder(g_coeffs), x) * hx - np.polyval(np.polyder(h_coeffs), x) * gx
    denominator = hx ** 2

    fx = numerator / denominator
    return fx