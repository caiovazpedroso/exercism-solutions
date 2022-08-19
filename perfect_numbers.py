'''
The Greek mathematician Nicomachus devised a classification scheme for positive
integers, identifying each as belonging uniquely to the categories of perfect, abundant,
or deficient based on their aliquot sum. The aliquot sum is defined as the sum of the factors of
a number not including the number itself. For example, the aliquot sum of 15 is (1 + 3 + 5) = 9
'''
def classify(number):
    """ A perfect number equals the sum of its positive divisors.

    :param number: int a positive integer
    :return: str the classification of the input integer
    """
    if number < 1:
        raise ValueError('Classification is only possible for positive integers.')
    i = 1
    total = 0
    while i < number:
        if number % i == 0:
            total += i
        i += 1
    if total == number:
        return 'perfect'
    elif total > number:
        return 'abundant'
    elif total < number:
        return 'deficient'

print(classify(28))