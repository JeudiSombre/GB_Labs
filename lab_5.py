from json import dump


def ex_1():
   with open("ex_1.txt", "a", encoding="utf-8") as t_file:
       while True:
        some_input = input("Введите любое значение, пустая строка считается окончанием ввода: ")
        if some_input == "":
            break
        t_file.write(some_input+"\n")


def ex_2():
    with open("ex_2.txt", "r", encoding="utf-8") as s_file:
        lines_count = 0
        for line_def in s_file:
            line = line_def.strip()
            lines_count += 1
            line_length = len(line)
            print(f"Row {lines_count} has {line_length}")
        print(f"Total rows {lines_count}")


def ex_3():
    with open("ex_3.txt", "r", encoding="utf-8") as s_file:
        cash = []
        for line_def in s_file:
            line = line_def.split()
            cash.append(float(line[1]))
            if float(line[1]) < 20000:
                print(line[0])
        print(sum(cash)/len(cash))


def ex_4():
    with open("ex_4.txt", "r", encoding="utf-8") as s_file:
        rus = {"1": "Один", "2": "Два", "3": "Три", "4": "Четыре"}
        for line_def in s_file:
            line = line_def.split(" — ")
            with open("ex_4_out.txt", "a") as t_file:
                print(f"{rus.get(line[1].strip())} — {line[1].strip()}", file=t_file)


def ex_5():
    with open("ex_5.txt", "w") as s_file:
        s_file.write("1.11 2 3.4 4")
    with open("ex_5.txt", "r") as s_file:
        print(sum(list(map(lambda x: float(x), s_file.read().split()))))


def ex_6():
    names = []
    time = []
    with open("ex_6.txt", "r", encoding="utf-8") as s_file:
        for line_def in s_file:
            line = line_def.split(":")
            names.append(line[0])
            nums = line[1].split()
            clean_nums = list(filter(None, map(lambda x: (''.join(i for i in x if i.isdigit())), nums)))
            time.append(sum(list(map(lambda x: int(x), clean_nums))))
    print(dict(zip(names, time)))


def ex_7():
    profit_names = []
    profit = []
    all_diff = []
    names = []
    output = []
    profit_num = 0
    with open("ex_7.txt", "r", encoding="utf-8") as s_file:
        for line_def in s_file:
            line = line_def.split()
            dif = int(line[2]) - int(line[3])
            names.append(line[0])
            all_diff.append(dif)
            if int(line[2]) >= int(line[3]):
                profit.append(dif)
                profit_num += 1
    output.append(dict(zip(names, all_diff)))
    output.append(dict(average_profit=sum(profit)/profit_num))
    with open("ex_7.json", "w") as write_f:
        dump(output, write_f, indent=4, ensure_ascii=False)


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
    if ex == '7':
        ex_7()


lab_check()
ans = input("Продолжаем проверку? (Да/Hет) ")
if ans == 'Да':
    lab_check()
elif ans == 'Нет':
    print('Хорошего дня')
else:
    print("Такого варианта нет!")