# lab prog
def ex_1():
    some_list = ['2', 1, ['2', 1], (1, '2'), {'1': 2}, {1, '2'}, True, frozenset([1, '2'])]
    for elem in some_list:
        print(type(elem))


def ex_2():
    some_input = input("Введите что-нибудь: ")
    i = 0
    k = 0
    some_list = []
    while i < len(some_input):
        some_list.append(some_input[i])
        i += 1
    if len(some_input) % 2 == 0:
        while k < len(some_input):
            some_list[k], some_list[k + 1] = some_list[k + 1], some_list[k]
            k += 2
    else:
        while k < len(some_input) - 2:
            some_list[k], some_list[k + 1] = some_list[k + 1], some_list[k]
            k += 2
    print(some_list)


def ex_3():
    some_input = input("Введите целое положительное число от 1 до 12:")
    seasons = {'autumn': ['9', '10', '11'], 'summer': ['6', '7', '8'], 'winter': ['12', '1', '2'],
               'spring': ['3', '4', '5']}
    season_val = ''
    try:
        if 1 <= int(some_input) < 12:
            for key, value in seasons.items():
                if some_input in value:
                    season_val = key
                    break
            print(season_val)
        else:
            print("Некорректное число")
    except ValueError:
        print("Некорректный ввод")


def ex_4():
    some_input = input("Введите строку из нескольких слов, разделенных пробелами: ")
    for i, elem in enumerate(some_input.split(),1):
        print(f"{i}) {elem}")


def ex_5():
    my_list = [7, 5, 3, 3, 2]
    some_input = input("Введите число: ")
    ind = 0
    if my_list.count(int(some_input)) > 1:
        my_list.insert(my_list.index(int(some_input)) + my_list.count(int(some_input)), int(some_input))
    else:
        for elem in my_list:
            if elem <= int(some_input) <= my_list[my_list.index(elem) - 1]:
                ind = my_list.index(elem)
            elif elem >= int(some_input) and my_list.index(elem) == my_list.index(my_list[-1]):
                ind = my_list.index(my_list[-1])+1
        my_list.insert(ind, int(some_input))
    print(my_list)


def ex_6():
    i = 1
    some_list = []
    clients_list = []
    age_list = []
    rate_list = []
    while i <= 3:
        clients = input("Введите имя клиента: ")
        age = int(input("Введите возраст клиента: "))
        rate = int(input("Введите рейтинг клиента: "))
        turple_add = (i, {'name': clients, 'age': age, 'rate': rate})
        some_list.append(turple_add)
        i += 1
    for elem in some_list:
        clients_list.append(elem[1].get('name'))
        age_list.append(elem[1].get('age'))
        rate_list.append(elem[1].get('rate'))
    some_dict = {'name': clients_list, 'age': age_list, 'rate': rate_list}
    print(some_dict)


def lab_check():
    ex = input("Введите упражнение для проверки: ")
    if ex == '1':
        ex_1()
    if ex == '2':
        ex_2()
    if ex == '3':
        ex_3()
    if ex == '4':
        ex_4()
    if ex == '5':
        ex_5()
    if ex == '6':
        ex_6()


lab_check()
ans = input("Продолжаем проверку? (Да/Hет) ")
if ans == 'Да':
    lab_check()
elif ans == 'Нет':
    print('Хорошего дня')
else:
    print("Такого варианта нет!")
