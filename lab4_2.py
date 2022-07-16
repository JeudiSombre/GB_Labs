some_list = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]


def get_prev(in_list, elem):
    return in_list[in_list.index(elem)-1]


new_list = [elem for elem in some_list if elem > get_prev(some_list, elem) and some_list.index(elem) != 0]
print(new_list)
