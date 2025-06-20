def is_triangle(a, b, c):
    """
    Check if three lengths can form a triangle.
    
    Triangle Inequality Theorem:
    The sum of any two sides must be greater than the third side.
    """
    # Check all sides are positive numbers
    if not all(isinstance(side, (int, float)) for side in [a, b, c]):
        return False
    
    if a <= 0 or b <= 0 or c <= 0:
        return False
    
    # Check triangle inequality
    return a + b > c and a + c > b and b + c > a