'''
Determine if a triangle is equilateral, isosceles, or scalene.
An equilateral triangle has all three sides the same length.
An isosceles triangle has at least two sides the same length.
A scalene triangle has all sides of different lengths.
a + b ≥ c
b + c ≥ a
a + c ≥ b
'''
def triangle(sides):
    a,b,c = sorted(sides)
    if  a + b >= c and\
        0 not in sides:
        return True
    return False

def equilateral(sides):
    a,b,c = sorted(sides)
    if triangle(sides):
        if a == b == c:
            return True
    return False

def isosceles(sides):
    a,b,c = sorted(sides)
    if triangle(sides):
        if a == b or\
        b == c or\
        c == a:
            return True
    return False

def scalene(sides):
    a,b,c = sorted(sides)
    if triangle(sides):
        if a != b and\
        b != c and\
        c != a:
            return True
    return False

print(equilateral([0,0,0]))