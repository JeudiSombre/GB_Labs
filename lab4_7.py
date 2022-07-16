from itertools import count
from math import factorial


def fact():
    for el in count(1):
        yield factorial(el)


i = 1
for el in fact():
    print(el)
    i += 1
    if i > 10:
        break
