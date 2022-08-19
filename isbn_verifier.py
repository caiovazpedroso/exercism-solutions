import string
'''
The ISBN-10 format is 9 digits (0 to 9) plus one check character (either a digit or an X only).
In the case the check character is an X, this represents the value '10'. These may be
communicated with or without hyphens, and can be checked
for their validity by the following formula:
(d₁ * 10 + d₂ * 9 + d₃ * 8 + d₄ * 7 + d₅ * 6 + d₆ * 5 + d₇ * 4 + d₈ * 3 + d₉ * 2 + d₁₀ * 1) mod 11
Given a string the program should check if the provided string is a valid ISBN-10.
Putting this into place requires some thinking about preprocessing/parsing of the string
prior to calculating the check digit for the ISBN.

The program should be able to verify ISBN-10 both with and without separating dashes.
'''
ints = [1,2,3,4,5,6,7,8,9,0]

def is_valid(isbn: str):
    indice = 10
    sigma = 0
    for digit in isbn:
        if digit == '-' or digit == ' ':
            continue
        elif digit.upper() in string.ascii_uppercase:
            if digit == 'X' and indice == 1:
                sigma += 10 * indice
                indice -= 1
            else:
                return False
        elif int(digit) in ints:
            sigma += (int(digit) * indice)
            indice -= 1
    if sigma != 0 and sigma % 11 == 0 and indice == 0 :
        return True
    return False

print(is_valid('3-598-21507-X'))