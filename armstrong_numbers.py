'''
An Armstrong number is a number that is the sum of its own digits each raised to the power of the number of digits.
'''
def is_armstrong_number(number):
    '''
    pass
    '''
    num_of_digits = len(str(number))
    i = test = 0
    while i < num_of_digits:
        test += int(str(number)[i]) ** num_of_digits
        i += 1
    return number == test
