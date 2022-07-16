from itertools import count, cycle


for el in count(3):
    if el > 10:
        break
    else:
        print(el)
some_list = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]
i = 1
for el in cycle(some_list):
    if i > len(some_list):
        break
    else:
        print(el)
        i += 1

