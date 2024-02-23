from src.Figure import Figure
from math import pi


class Circle(Figure):
    def __init__(self, side_a):
        super().__init__(name="Circle")
        if side_a <= 0:
            raise ValueError("нельзя создать круг")
        self.side_a = side_a

    def get_area(self):
        diameter = self.side_a
        radius = diameter / 2
        area = pi * (radius ** 2)
        return round(area, 2)

    def get_perimetr(self):
        diameter = self.side_a
        radius = diameter / 2
        perimetr = round(2 * pi * radius, 2)
        return perimetr
