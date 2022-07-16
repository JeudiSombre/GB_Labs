from functools import reduce


def my_f(prev_el, el):
    return prev_el*el


print(reduce(my_f, [e for e in range(100, 1001)]))
