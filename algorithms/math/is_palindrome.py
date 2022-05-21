def is_palindrome(n: int) -> bool:
    """
    Checks if the input num is a palindrome
    """

    n = abs(n)
    num: int = n
    rev: int = 0

    while n > 0:
        rev = (10 * rev) + (n % 10)
        n //= 10

    return num == rev