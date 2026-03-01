def gradient_descent_quadratic(a, b, c, x0, lr, steps):
    """
    Return final x after 'steps' iterations.
    """
    # Write code here
    xf = 0
    xi = x0
    for i in range(steps):
        xf = xi - lr*(2*a*xi + b)
        xi = xf
    return xf