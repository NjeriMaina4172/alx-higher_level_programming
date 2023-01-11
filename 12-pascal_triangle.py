#!/usr/bin/python3
""" module: factorial """


def factorial(n):
    """ function to get the factorial of a number
    Args:
        @n: the value
    """
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)


def pascal_triangle(n):
    """ pascal triangle
    Args:
        @n: the value of the triangle table
    """
    if n <= 0:
        return []

    bigger_list = []
    for k in range(1, n + 1):
        lst = []
        for i in range(0, k):
            val = int(factorial(k - 1) / (factorial(i) * factorial(k - i - 1)))
            lst.append(val)
        bigger_list.append(lst)
    return (bigger_list)
    