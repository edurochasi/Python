from math import pi


def arc_length(ag: int, rd: int) -> float:
    """
    >>> arc_length(45, 5)
    3.9269908169872414
    >>> arc_length(120, 15)
    31.415926535897928
    """
    return 2 * pi * rad * (ang / 360)


if __name__ == "__main__":
    print(arc_length(90, 10))
