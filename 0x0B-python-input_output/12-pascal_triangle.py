#!/usr/bin/python3
"""----- 12. Pascal's Triangle -----
    Function that returns a list of lists of integers representing
    the Pascal’s triangle of n
"""


def pascal_triangle(n):
    """----- pascal_triangle function -----
        returns a list of lists of integers representing the
        Pascal’s triangle of n
        Args:
            n: must be integer
        Returns:
            Nothing.
    """
    p_list = []
    trow = [1]
    y = [0]
    for x in range(n):
        p_list.append(trow)
        trow = [left + right for left, right in zip(trow + y, y + trow)]
    return p_list
