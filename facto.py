# def factorial(n: int) -> int:
#     """Return n! (0! is 1)."""
#     if n <= 1:
#         return 1
 
#     result = 2
#     for x in range(3, n + 1):
#         result *= x
 
#     return result
 
 
# for i in range(36):
#     print(i, factorial(i))


def factorial(n: int) -> int:
    """
    Return n! (0! is 1).
 
    Valid for `n` in the range 0 to 998 (inclusive).
    Larger values of `n` will cause a RecursionError.
    """
    if n <= 1:
        return 1
 
    return n * factorial(n - 1)


for i in range(11):
    print(i, factorial(i))
