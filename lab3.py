# exercise 1
def ex_1(*args):
    return 'Результат деления первого числа на второе ' + str(float(args[0]) / float(args[1]))


try:
    print(ex_1(input('Введите первое число: '), input('Введите второе число: ')))
except ZeroDivisionError:
    print('Делить на ноль нельзя!')


# exercise 2
def ex_2(**kwargs):
    return kwargs


print(ex_2(name=input('Имя: '), surname=input('Фамилия: '), birthdate=input('Дата рождения: '),
           city=input('Место жительства: '), email=input('email: '), phone=input('телефон: ')))


# exercise 3
def ex_3(*args):
    some_list = list(map(float, [args[0], args[1], args[2]]))
    some_list.sort()
    some_list.pop(0)
    return str(sum(some_list))


try:
    print('Результат: '+ex_3(input('Введите первое число: '), input('Введите второе число: '), input('Введите третье число: ')))
except ValueError:
    print("Ошибка ввода, принимаются только числа")


# exercise 4
def ex_4(x, y):
    res = 1
    i = 1
    while i <= abs(y):
        res = res*x
        i += 1
    return str(1/res)


try:
    x = float(input('Введите действительное положительное число: '))
    y = int(input('Введите целое отрицательное число: '))
    if abs(x)-x != 0:
        raise Exception('Первое число должно быть положительным')
    if abs(y)+y != 0:
        raise Exception('Второе число должно быть отрицательным')
    print('Результат: '+ex_4(x, y))
except ValueError:
    print('Второе число должно быть целым')
except Exception as ex:
    print(ex)


# exercise 5
def ex_5():
    some_list = []
    print('Введите строку чисел, разделённых пробелом: ')
    try:
        while True:
            some_input = input()
            if 'q' in some_input:
                if some_input.index('q') > 0:
                    some_list.extend(map(float, some_input[:some_input.index('q')-1].split()))
                    print(sum(some_list))
                break
            some_list.extend(map(float, some_input.split()))
            print(sum(some_list))
    except ValueError:
        print('Err')


ex_5()


# exercise 6
def ex_6(some_string, num):
    alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
                'v', 'w', 'x', 'y', 'z']
    try:
        result = some_string.title()
        if some_string.islower() == 0:
            raise Exception(f"В {num} слове есть символы в верхнем регистре!")
        if some_string.isalpha() == 0:
            raise Exception(f"В {num} слове есть цифры!")
        for elem in some_string:
            if elem not in alphabet:
                raise Exception(f"В {num} слове есть не латинские символы!")
    except Exception as ex:
        print(ex)
        return ''
    else:
        return result


x = input('Введите строку из слов, состоящих из маленьких латинских букв: ')
input_list = x.split()
output_list = []
i = 1
for el in input_list:
    output_list.append(ex_6(el, i))
    i += 1
print(' '.join([i for i in output_list if i]))

