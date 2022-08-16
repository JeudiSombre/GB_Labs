# ex 1
from functools import reduce
class Matrix:
    def __init__(self, obj=[[1, 1, 1], [1, 1, 1], [1, 1, 1], [1, 1, 1]]):
        self.obj = obj

    def check(self):
        try:
            if reduce(lambda x, y: x if len(x) == len(y) else y, self.obj) != self.obj[0]:
                raise Exception('Матрица некорректна!')
            return True
        except Exception as ex:
            print(ex)

    def __str__(self):
        new_string = '\n'
        return f"{new_string.join(' '.join(list(map(lambda x: str(x),n))) for n in self.obj)}"

    def __add__(self, other):
        try:
            if len(self.obj) != len(other.obj) or len(self.obj[0]) != len(other.obj[0]) or self.check() is not True or other.check() is not True:
                raise Exception('Матрицы разной размерности!')
            return Matrix(list(map(lambda x, y: x + y, self.obj[n], other.obj[n])) for n in range(0, len(self.obj)))
        except Exception as ex:
            print(ex)

m = Matrix()
n = Matrix([[2, 3, 1], [4, 5, 1], [6, 7, 1], [6, 7, 1]])
print(m+n)
# ex 2
from abc import ABC, abstractmethod
class Cloth(ABC):
    def __init__(self, input):
        self.input = input

    @abstractmethod
    def cost(self):
        pass


class Coat(Cloth):
    @property
    def cost(self):
        return self.input/6.5 + 0.5


class Costume(Cloth):
    @property
    def cost(self):
        return self.input*2 + 0.3
palto = Coat(6.5)
costume = Costume(1.1)
print(costume.cost)
print(palto.cost)
print(costume.cost+palto.cost)

# ex 3
class Cell:
    def __init__(self, n):
        self.n = n

    def __str__(self):
        return f"{self.n}"

    def __add__(self, other):
        return Cell(self.n + other.n)

    def __sub__(self, other):
        if self.n - other.n > 0:
            return Cell(self.n - other.n)
        else:
            print("Поменяйте клетки местами и проверьте что они разного размера.")

    def __mul__(self, other):
        return Cell(self.n * other.n)

    def __truediv__(self, other):
        return Cell(self.n//other.n)

    def make_order(self, nr ):
        return '\n'.join(['*'*nr for i in range(self.n//nr)])+'\n'+'*'*(self.n % nr)

a = Cell(11)
b = Cell(2)
print(a-b)
print(a+b)
print(a*b)
print(a/b)
print(a.make_order(2))
