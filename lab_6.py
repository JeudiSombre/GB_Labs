# ex 1:
from time import sleep


class TrafficLight:
    __color = ""

    def running(self):
        colors = {"red": 7, "yellow": 2, "green": 10}
        while True:
            for key, value in colors.items():
                self.__color = key
                print(f"{self.__color}")
                sleep(value)


svetofor = TrafficLight()
svetofor.running()

# 2 ex:
class Road:
    mass_sm = 10
    sm = 1000

    def __init__(self, length, width):
        self._length = length
        self._width = width

    def get_mass(self):
        print(self._length*self._width*Road.mass_sm*Road.sm)


yaroslavka = Road(250000, 3000)
yaroslavka.get_mass()

# 3 ex:
class Worker:
    def __init__(self, name, surname, position, wage, bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {"wage": wage, "bonus": bonus}


class Position(Worker):
    def get_full_name(self):
        return f"{self.name} {self.surname}"

    def get_full_profit(self):
        return sum(self._income.values())


sisadmin = Position("Karl", "Marks", "Sistemnii administrator", 80000, 20000)
print(f"{sisadmin.get_full_name()} has {sisadmin.get_full_profit()} rubles")

# 4 ex:
from random import choice


class Car:
    direction = ["N", "E", "W", "S", "NE", "NW", "NS", "SE", "SW"]

    def __init__(self, speed, color, name, is_police=False):
        self.speed = speed
        self.color = color
        self.is_police = is_police
        self.name = name
        print(f"Name:{self.name},Color:{self.color},Police:{self.is_police}")
        print('-------*-------*--------')

    def go(self):
        print(f"{self.name} started moving.")

    def stop(self):
        print(f"{self.name} stopped moving.")

    def turn(self):
        print(f"{self.name} turned to {choice(Car.direction)}.")

    def show_speed(self):
        return f"{self.name} speed is {self.speed}."


class TownCar(Car):

    def show_speed(self):
        return f"{self.name} speed is {self.speed}, speeding!" if self.speed > 60 else super().show_speed()


class WorkCar(Car):

    def show_speed(self):
        return f"{self.name} speed is {self.speed}, speeding!" if self.speed > 40 else super().show_speed()


class SportCar(Car):
    """ something """


class PoliceCar(Car):

    def __init__(self, speed, color, name):
        super().__init__(speed, color, name, is_police=True)


pol_car = PoliceCar(100, 'blue', '"Bobik"')
work_car = WorkCar(50, 'white', '"Gazel"')
sport_car = SportCar(150, 'yellow', '"reno"')
town_car = TownCar(60, 'white', '"Gazel"')
cars = [pol_car, work_car, sport_car, town_car]
for el in cars:
    el.go()
    el.stop()
    el.turn()
    print(el.show_speed())
    print('-------*-------*--------')

# ex 5
class Stationery:
    def __init__(self, title="unrecognized drawing thing"):
        self.title = title

    def draw(self):
        print(f"Trying to write down something with {self.title}")


class Pen(Stationery):
    def draw(self):
        print(f"Start writing with {self.title}.Cool pen!")


class Pencil(Stationery):
    def draw(self):
        print(f"Start drawing with {self.title}.Cool pencil!")


class Handle(Stationery):
    def draw(self):
        print(f"Start painting with {self.title}.Cool handle!")


something = Stationery()
pen = Pen("blue pen")
pencil = Pencil("pencil lead")
handle = Handle("yellow handle")
drawings = [something, pen, pencil, handle]
for el in drawings:
    el.draw()
    print('-------*-------*--------')