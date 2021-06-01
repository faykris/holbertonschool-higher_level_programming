#!/usr/bin/python3
def matrix_mul(m_a, m_b):

    if type(m_a) is not list:
        raise TypeError("m_a must be a list")
    if type(m_b) is not list:
        raise TypeError("m_b must be a list")

    for num in m_a:
        if type(num) is not list:
            raise TypeError("m_a must be a list of lists")
    for num in m_b:
        if type(num) is not list:
            raise TypeError("m_b must be a list of lists")

    if m_a == [] or m_a == [[]]:
        raise ValueError("m_a should contain only integers or floats")
    if m_b == [] or m_b == [[]]:
        raise ValueError("m_b should contain only integers or floats")

    for array in m_a:
        for num in array:
            if type(num) is not int and type(num) is not float:
                raise TypeError("m_a should contain only integers or floats")
    for array in m_b:
        for num in array:
            if type(num) is not int and type(num) is not float:
                raise TypeError("m_b should contain only integers or floats")

    a_len = 0
    for array in m_a:
        if a_len != len(array) and a_len != 0:
            raise TypeError("each row of m_a must be of the same size")
        else:
            a_len = len(array)
    b_len = 0
    for array in m_b:
        if b_len != len(array) and b_len != 0:
            raise TypeError("each row of m_b must be of the same size")
        else:
            b_len = len(array)

    return m_a
