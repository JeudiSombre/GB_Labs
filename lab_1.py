#lab prog
def ex_1():
    some_input=input("Введите число или фразу: ")
    print('Вы ввели: {}'.format(some_input))
    
def ex_2():
    some_input=input("Введите время в секундах: ")
    hh=f"{int(some_input)//3600:0>2}"
    mm=f"{(int(some_input)%3600)//60:0>2}"
    ss=f"{(int(some_input)%3600)%60:0>2}"
    some_string="{}:{}:{}".format(hh,mm,ss)
    print(some_string)
    
def ex_3():
    n=input("Введите число:")
    print(str(int(n)+int(n+n)+int(n+n+n)))

def ex_4():
    n=int(input("Введите целое положительное число: "))
    i=n%10
    while n//10!=0:
        n=n//10
        if i<n%10:
            i=n%10
    print(i)

def ex_5():
    cash=int(input("Введите выручку фирмы: "))
    costs=int(input("Введите издержки фирмы: "))
    if cash>costs:
        print('Прибыль')
        print('Рентабельность {}'.format('{:.2f}%'.format(cash/costs)))
        workers=int(input("Введите количество сотрудников: "))
        print('На одного сотрудника приходится прибыли в размере:{}'.format(cash/workers))
    elif cash<costs:
        print('Убыток')
    else:
        print('Точка безубыточности и бесприбыльности')
    
def ex_6():
    start=int(input("Введите результат в первый день: "))
    stop=int(input("Введите желаемый результат: "))
    day=1
    gros=start
    while True:
        gros=gros+gros*0.1
        day+=1
        if gros>=stop:
            break
    print("на {} день спортсмен достиг результата — не менее {} км.".format(day,stop))

def lab_check():
    ex=input("Введите упражнение для проверки: ")
    if ex=='1':
       ex_1() 
    if ex=='2':
       ex_2()
    if ex=='3':
       ex_3()
    if ex=='4':
       ex_4()
    if ex=='5':
       ex_5()
    if ex=='6':
       ex_6()
       
lab_check()
ans=input("Продолжаем проверку? (Да/Hет) ")
if ans=='Да':
    lab_check()
elif ans=='Нет':
    print('Хорошего дня')
else:
    print("Такого варианта нет!")