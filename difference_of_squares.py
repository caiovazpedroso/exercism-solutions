'''
Find the difference between the square of the sum and the sum of the squares of the first N natural numbers.

The square of the sum of the first ten natural numbers is (1 + 2 + ... + 10)² = 55² = 3025.

The sum of the squares of the first ten natural numbers is 1² + 2² + ... + 10² = 385.

Hence the difference between the square of the sum of the first ten natural numbers and the sum of the squares of the first ten natural numbers is 3025 - 385 = 2640.
'''
def square_of_sum(number):
    i = total = 0
    while i <= number:
        total += i
        i += 1
    return total**2

def sum_of_squares(number):
    i = total = 0
    while i <= number:
        total += i**2
        i += 1
    return total


def difference_of_squares(number):
    return square_of_sum(number) - sum_of_squares(number)