import random
from fractions import Fraction

# int
def generate_whole_num():
    return random.randint(1, 10000)

# decimal
def generate_decimal_num():
    return round(random.random(), 5)

# fractions
def generate_fraction_num():
    return Fraction(random.randint(1, 100), random.randint(1, 10000))

# negative
def generate_negative_num():
    return random.randint(-10000, -1)
