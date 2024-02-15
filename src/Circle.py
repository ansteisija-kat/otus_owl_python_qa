from src.Square import Square
from math import pi


class Circle(Square):
    def __init__(self, side_a):
        if side_a <= 0:
            raise ValueError("нельзя создать круг")
        super().__init__(side_a)

    def get_area(self):
        diameter = self.side_a
        radius = diameter / 2
        area = pi * (radius ** 2)
        return round(area, 2)

    def get_perimetr(self):
        diameter = self.side_a
        radius = diameter / 2
        perimetr = 2 * pi * radius
        return perimetr
