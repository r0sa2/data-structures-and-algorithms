from math import log10

def count_digits(n: int) -> int:
    """
    Computes the no of digits of the input num
    """
    return (int(log10(abs(n))) + 1) if n != 0 else 1