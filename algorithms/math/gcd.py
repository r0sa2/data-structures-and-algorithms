def gcd(n: int, m: int) -> int:
    """
    Computes the greatest common divisor (GCD) of the input nums using the 
    Euclidean algorithm
    """
    n, m = abs(n), abs(m)
	
    return gcd(m, n % m) if m != 0 else n