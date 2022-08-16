# ex 1
class Date:
    def __init__(self, input):
        self.input = input
    @classmethod
    def toint(cls, input):
        return cls(int(input.replace('-', '')))

    @staticmethod
    def check(obj):
        some_list = obj.input.split('-')
        if 1 <= int(some_list[0]) <= 31 and 1 <= int(some_list[1]) <= 12 and 0 < int(some_list[2]):
            return 'Date is valid'
        else:
            return 'Date is not valid'

d = Date('30-01-1999')
print(d.input)
da = Date.toint('31-01-1999')
print(da.input)
print(Date.check(d))

#ex 2
class Custex(Exception):
 def __str__(self):
        return "Devide by zero is restricted."


a = input('Vvedite delimoe: ')
b = input('Vvedite delitel: ')
try:
    if int(b) == 0:
        raise Custex
except Custex:
    print(Custex())
else:
    print(str(int(a)/int(b)))

# ex 3
class Custex_1(Exception):
 def __str__(self):
        return "Invalid insert."

some_list = []
while True:
    a = input('Vvedite chislo: ')
    try:
        if not a.isdigit():
            raise Custex_1
    except Custex_1:
        print(Custex_1())
    else:
        some_list.append(a)
    if a =='stop':
        print(some_list)
        break
# ex 4,5,6
from abc import abstractmethod


class Warehouse:
    def __init__(self):
        self.items = []

    def items_stored(self):
        return self.items

    def add_items(self, *items):
        self.items.extend(items)

class Org:
    def __init__(self, model, number):
        self.model = model
        self.number = number
        if type(number) != type(1):
            raise NotNumber(number)
    @abstractmethod
    def to_store(self, customer):
        pass


class Printer(Org):
    def __init__(self, model, number, printer_type):
        super().__init__(model, number)
        self.items = []
        self.printer_type = printer_type

    def to_store(self, customer):
        self.items.append({'Printers': {'Department': customer, 'Model': self.model, 'Number': self.number,
                                      'Type': self.printer_type}})
        return self.items[0]


class Scaner(Org):
    def __init__(self, model, number, scaner_type):
        super().__init__(model, number)
        self.items = []
        self.scaner_type = scaner_type

    def to_store(self, customer):
        self.items.append({'Scaners': {'Department': customer, 'Model': self.model, 'Number': self.number,
                                        'Type': self.scaner_type}})
        return self.items[0]


class Kseroks(Org):
    def __init__(self, model, number, kseroks_type):
        super().__init__(model, number)
        self.items = []
        self.kseroks_type = kseroks_type

    def to_store(self, customer):
        self.items.append({'Kseroks': {'Department': customer, 'Model':self.model, 'Number': self.number, 'Type': self.kseroks_type}})
        return self.items[0]

class Department:
    def __init__(self, name):
        self.name = name
        self.env = []
    def take(self, doc):
        self.env.extend([x for x in doc if x.get(list(x.keys())[0]).get("Department") == self.name])
        return f'Department {self.name} get from warehouse {self.env}'

class NotNumber(Exception):
    def __init__(self, number):
        self.number = number

    def __str__(self):
        return f'Invalid number!'


w = Warehouse()
try:
    p = Printer('p1', 2, 'laser')
    s = Scaner('s1', 3, 'hand')
    k = Kseroks('k1', 6, 'chb')
    w.add_items(p.to_store('managers'), s.to_store('managers'), k.to_store('office'))
except NotNumber as er:
    print(er)
    print(f'You inserted {type(er.number)} instead of real number. Fix it.')
d_1 = Department('managers')
d_2 = Department('office')
print(w.items_stored())
print(d_2.take(w.items_stored()))
print(d_1.take(w.items_stored()))

# ex 7
class Complex:
    def __init__(self, input):
        self.input = input
        self.a = int(input.split("+")[0])
        self.a_m = int(input.split("+")[1][:-1])

    def __add__(self, other):
        return Complex(f'{self.a+other.a}+{self.a_m + other.a_m}i')

    def __mul__(self, other):
        return Complex(f'{self.a*other.a -self.a_m*other.a_m }+{other.a*self.a_m + self.a*other.a_m}i')

    def __str__(self):
        return f'{self.input}'


f = Complex('1+2i')
s = Complex('4+4i')
print(f*s)
print(f+s)
