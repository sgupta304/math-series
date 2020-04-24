def fibonacci(index):
    return sum_series(index, 0, 1)


def lucas(index):
    return sum_series(index, 2, 1)


def sum_series(index, a=0, b=1):
    if index == 0:
        return a
    if index == 1:
        return b
    return sum_series(index - 1, a, b) + sum_series(index - 2, a, b)
