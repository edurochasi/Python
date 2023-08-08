def average_absolute_deviation(nums: list[int]) -> float:
    """
    >>> average_absolute_deviation([0])
    0.0
    """
    if not nums:  # Makes sure that the list is not empty
        raise ValueError("List is empty")

    average = sum(nums) / len(nums)  # Calculate the average
    return sum(abs(x - average) for x in nums) / len(nums)


if __name__ == "__main__":
    import doctest

    doctest.testmod()
