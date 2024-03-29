from src.Figure import Figure
from math import sqrt


class Triangle(Figure):
    def __init__(self, side_a, side_b, side_c):
        super().__init__(name="Triangle")
        if side_a <= 0 or side_b <= 0 \
                or side_c <= 0:
            raise ValueError("нельзя создать треугольник")
        elif (side_a + side_b) <= side_c \
                or (side_a + side_c) <= side_b \
                or (side_b + side_c) <= side_a:
            raise ValueError("нельзя создать треугольник")
        self.side_a = side_a
        self.side_b = side_b
        self.side_c = side_c

    def get_area(self):
        half_perimetr = (self.side_a + self.side_b + self.side_c) / 2
        area = sqrt(half_perimetr * (half_perimetr - self.side_a) * (half_perimetr - self.side_b)
                    * (half_perimetr - self.side_c))
        return round(area, 2)

    def get_perimetr(self):
        return self.side_a + self.side_b + self.side_c
