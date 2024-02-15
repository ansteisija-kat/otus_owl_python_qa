from Rectangle import Rectangle


class Square(Rectangle):
    def __init__(self, side_a):
        if side_a <= 0:
            raise ValueError("нельзя создать квадрат")
        super().__init__(side_a, side_a)

    def get_area(self):
        return self.side_a ** 2

    def get_perimetr(self):
        return self.side_a * 4

s = Square(3)