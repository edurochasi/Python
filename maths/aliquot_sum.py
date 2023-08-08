def aliquot_sum(input_num: int) -> int:
    """
    Finds the aliquot sum of an input integer, where the
    aliquot sum of a number n is defined as the sum of all
    natural numbers less than n that divide n evenly. For
    example, the aliquot sum of 15 is 1 + 3 + 5 = 9. This is
    a simple O(n) implementation.

    >>> aliquot_sum(15)
    9
    >>> aliquot_sum(6)
    6
    """
    if not isinstance(input_num, int):
        raise ValueError("Input must be an integer")
    if input_num <= 0:
        raise ValueError("Input must be positive")

    counter = 0
    last_limit = input_num//2 + 1
    for i in range(1, last_limit):
        if input_num % i == 0:
            counter += i
    return counter


if __name__ == "__main__":
    import doctest

    doctest.testmod()
