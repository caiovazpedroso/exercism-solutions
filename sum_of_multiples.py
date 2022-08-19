'''
Given a number, find the sum of all the unique multiples of
particular numbers up to but not including that number.

If we list all the natural numbers below 20 that are multiples
of 3 or 5, we get 3, 5, 6, 9, 10, 12, 15, and 18.

The sum of these multiples is 78.
'''

from os import remove


def sum_of_multiples(limit, multiples):
    n = a = 0
    total = []
    if 0 in multiples:
        multiples.remove(0)
    while n < limit:
        for a in multiples:
            if n % a == 0:
                if n not in total:
                    total.append(n)
        n += 1
    return sum(total)

print(sum_of_multiples(20,[3,5]))