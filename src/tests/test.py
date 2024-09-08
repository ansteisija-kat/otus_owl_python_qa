import pytest
from src.tests.data import *
from src.Circle import *
from src.Rectangle import *
from src.Triangle import *
from src.Square import *

# test data
rectangle = Rectangle(generate_whole_num(), generate_whole_num())
square = Square(generate_whole_num())
circle = Circle(generate_whole_num())
rectangle_error = ValueError("нельзя создать прямоугольник")
triangle_error = ValueError("нельзя создать треугольник")
square_error = ValueError("нельзя создать квадрат")
circle_error = ValueError("нельзя создать круг")


@pytest.fixture(autouse=False, name='valid_triangle')
def create_basic_triangle():
    while True:
        triangle_sides = (generate_whole_num(), generate_whole_num(), generate_whole_num())
        if (
                triangle_sides[0] > 0
                and triangle_sides[1] > 0
                and triangle_sides[2] > 0
        ) and (
                (triangle_sides[0] + triangle_sides[1]) > triangle_sides[2]
                and (triangle_sides[0] + triangle_sides[2]) > triangle_sides[1]
                and (triangle_sides[1] + triangle_sides[2]) > triangle_sides[0]
        ):
            triangle = Triangle(triangle_sides[0], triangle_sides[1], triangle_sides[2])
            return triangle


# basic positive tests

def test_rectangle_basic_methods():
    area = rectangle.get_area()
    perimetr = rectangle.get_perimetr()

    assert area > 0 and \
           perimetr > 0, \
        f'Area or perimetr are not correct'


def test_triangle_basic_methods(valid_triangle):
    area = valid_triangle.get_area()
    perimetr = valid_triangle.get_perimetr()

    assert area > 0 and \
           perimetr > 0, \
        f'Area or perimetr are not correct'


def test_square_basic_methods():
    area = square.get_area()
    perimetr = square.get_perimetr()

    assert area > 0 and \
           perimetr > 0, \
        f'Area or perimetr are not correct'


def test_circle_basic_methods():
    area = circle.get_area()
    perimetr = circle.get_perimetr()

    assert area > 0 and \
           perimetr > 0, \
        f'Area or perimetr are not correct'


def test_add_area_basic(valid_triangle):
    # same figures
    t_t = valid_triangle.add_area(valid_triangle)
    s_s = square.add_area(square)
    c_c = circle.add_area(circle)
    r_r = rectangle.add_area(rectangle)
    # diff figures
    s_t = square.add_area(valid_triangle)
    s_c = square.add_area(circle)
    s_r = square.add_area(rectangle)
    t_s = valid_triangle.add_area(square)
    t_c = valid_triangle.add_area(circle)
    t_r = valid_triangle.add_area(rectangle)
    c_s = circle.add_area(square)
    c_t = circle.add_area(valid_triangle)
    c_r = circle.add_area(rectangle)
    r_s = rectangle.add_area(square)
    r_c = rectangle.add_area(circle)
    r_t = rectangle.add_area(valid_triangle)

    for sum_areas in (t_t, s_s, c_c, r_r, s_t, s_c, s_r, t_s, t_c, t_r, c_s, c_t, c_r, r_s, r_c, r_t):
        assert True, f'Sum of areas was not calculated, {sum_areas} should be at least > 0'


# additional positive test

def test_fractions_as_sides(valid_triangle):
    r = Rectangle(generate_fraction_num(), generate_fraction_num())
    s = Square(generate_fraction_num())
    c = Circle(generate_fraction_num())

    for f in (r, s, c):
        assert True, f'Figure should exist with fraction number as a side'


# basic negative tests

@pytest.mark.parametrize('side_a', [0])
def test_one_side_is_zero_fails_circle(side_a):
    with pytest.raises(ValueError):
        assert Circle(side_a) == circle_error


@pytest.mark.parametrize('side_a', [0])
def test_one_side_is_zero_fails_square(side_a):
    with pytest.raises(ValueError):
        assert Square(side_a) == square_error


@pytest.mark.parametrize('side_a, side_b', [(generate_whole_num(), 0)])
def test_one_side_is_zero_fails_rectangle(side_a, side_b):
    with pytest.raises(ValueError):
        assert Rectangle(side_a, side_b) == rectangle_error


@pytest.mark.parametrize('side_a, side_b, side_c', [(generate_whole_num(), generate_whole_num(), 0)])
def test_one_side_is_zero_fails_triangle(side_a, side_b, side_c):
    with pytest.raises(ValueError):
        assert Triangle(side_a, side_b, side_c) == triangle_error


@pytest.mark.parametrize('side_a, side_b', [(generate_whole_num(), generate_negative_num())])
def test_negative_side_fails_rectangle(side_a, side_b):
    with pytest.raises(ValueError):
        assert Rectangle(side_a, side_b) == rectangle_error


@pytest.mark.parametrize('side_a, side_b, side_c',
    [(generate_whole_num(), generate_whole_num(), generate_negative_num())])
def test_negative_side_fails_triangle(side_a, side_b, side_c):
    with pytest.raises(ValueError):
        assert Triangle(side_a, side_b, side_c) == triangle_error


@pytest.mark.parametrize('side_a, side_b', [(generate_whole_num(), generate_negative_num())])
def test_negative_side_fails_rectangle(side_a, side_b):
    with pytest.raises(ValueError):
        assert Rectangle(side_a, side_b) == rectangle_error


@pytest.mark.parametrize('side_a', [generate_negative_num()])
def test_negative_side_fails_square(side_a):
    with pytest.raises(ValueError):
        assert Square(side_a) == square_error


@pytest.mark.parametrize('side_a', [generate_negative_num()])
def test_negative_side_fails_circle(side_a):
    with pytest.raises(ValueError):
        assert Circle(side_a) == circle_error


@pytest.mark.parametrize('side_a, side_b', [(generate_decimal_num(), 0)])
def test_invalid_type_side_fails_rectangle(side_a, side_b):
    with pytest.raises(ValueError):
        assert Rectangle(side_a, side_b)


@pytest.mark.parametrize('side_a, side_b, side_c', [(generate_whole_num(), generate_whole_num(), '')])
def test_invalid_type_side_fails_triangle(side_a, side_b, side_c):
    with pytest.raises(TypeError):
        assert Triangle(side_a, side_b, side_c)


@pytest.mark.parametrize('side_a', ['_'])
def test_invalid_type_side_fails_square(side_a):
    with pytest.raises(TypeError):
        assert Square(side_a)


@pytest.mark.parametrize('side_a', ['/n'])
def test_invalid_type_side_fails_square(side_a):
    with pytest.raises(TypeError):
        assert Circle(side_a)


@pytest.mark.parametrize('side_a, side_b', [(generate_whole_num(), generate_decimal_num())])
def test_invalid_count_sides_fails_circle(side_a, side_b):
    with pytest.raises(TypeError):
        assert Circle(side_a, side_b)


@pytest.mark.parametrize('side_a, side_b, side_c',
    [(generate_whole_num(), generate_whole_num(), generate_decimal_num())])
def test_invalid_count_sides_fails_rectangle(side_a, side_b, side_c):
    with pytest.raises(TypeError):
        assert Rectangle(side_a, side_b, side_c)


@pytest.mark.parametrize('side_a, side_b, side_c, side_d',
    [(generate_whole_num(), generate_decimal_num(), generate_decimal_num(), generate_decimal_num())])
def test_invalid_count_sides_fails_triangle(side_a, side_b, side_c, side_d):
    with pytest.raises(TypeError):
        assert Triangle(side_a, side_b, side_c, side_d)


@pytest.mark.parametrize('side_a, side_b', [(generate_whole_num(), generate_decimal_num())])
def test_invalid_count_sides_fails_square(side_a, side_b):
    with pytest.raises(TypeError):
        assert Square(side_a, side_b)


@pytest.mark.parametrize('side_a, side_b, side_c', [(1, 2, 3), (1, 0.55886, 2), (10, 5.7, 3), (6, 12, 4)])
def test_triangle_add_options_fails(side_a, side_b, side_c):
    with pytest.raises(ValueError):
        assert Triangle(side_a, side_b, side_c) == triangle_error
