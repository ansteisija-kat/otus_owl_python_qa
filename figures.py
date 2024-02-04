# Описание:
# Создать базовый класс геометрической фигуры (Figure).
# Реализовать классы геометрических фигур
# Треугольник, Прямоугольник, Квадрат, Круг (Triangle, Rectangle, Square, Circle).
# Каждый класс должен располагаться в отдельном файле с соответствующим названием
# (например, class Triangle => triangle.py).
# у каждого класса должны быть методы get_area() - площадь и get_perimeter() - периметр
# Все файлы с классами должны находиться в директории src/ в корне репозитория.
# Треугольник должен задаваться тремя сторонами, если треугольник создать нельзя,
# то выбрасывать ошибку raise ValueError.
# Все вычисляемые свойства должны вычисляться по формулам для соответствующих геометрических фигур
# (никакого хардкода значений).
# Каждая фигура должна реализовать метод add_area(figure) который должен принимать другую геометрическую фигуру
# и возвращать сумму площадей этих фигур.
# Если в метод передана не геометрическая фигура, то нужно выбрасывать ошибку raise ValueError.

# Критерии оценки:
# Будет оцениваться глубина использования парадигмы ООП.
# Встроенные декораторы, наследование, отсутствие дублирования кода.
# Если какой-то метод выполняет одно и тоже во всех классах наследниках, то он должен принадлежать родительскому классу.
# Задание сдавать в формате pull-request.
# Соблюдение минимального кодстайла.
# Никаких print-ов, закомментированного кода и лишних файлов быть не должно.

from abc import ABC, abstractmethod


class Figure(ABC):
    def __init__(self, name):
        self.name = name

    @abstractmethod
    def get_area(self):
        pass

    @abstractmethod
    def get_perimetr(self):
        pass

    def add_area(self, other_figure):
        if not isinstance(other_figure, Figure):
            raise ValueError("Нужно передать фигуру")
        return self.get_area() + other_figure.get_area()


class Rectangle(Figure):
    def __init__(self, side_a, side_b, name):
        super().__init__(name="Rectangle")
        if side_a <= 0 or side_b <= 0:
            raise ValueError("нельзя создать прямоугольник")
        self.side_a = side_a
        self.side_b = side_b

    def get_area(self):
        return self.side_a * self.side_b

    def get_perimetr(self):
        return 2 * (self.side_a + self.side_b)


class Square(Rectangle):
    def __init__(self, side_a):
        if side_a <= 0:
            raise ValueError("нельзя создать квадрат")
        super().__init__(side_a, side_a)


s = Square(3)