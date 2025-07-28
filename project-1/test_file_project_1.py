def fibbonacci_number(n):
    """_Compute the nth Fibonacci number.

    Args:
        n: The position in the Fibonacci sequence.

    Returns:
        The nth Fibonacci number.
    """
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibbonacci_number(n - 1) + fibbonacci_number(n - 2)
        
