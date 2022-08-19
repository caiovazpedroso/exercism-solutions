'''
Create an implementation of the rotational cipher, also sometimes called the Caesar cipher.
'''
from string import ascii_lowercase, ascii_uppercase

lower_cipher = {}
upper_cipher = {}
i = j = 1
for letter in ascii_lowercase:
    lower_cipher[letter] = i
    i+=1
for letter in ascii_uppercase:
    upper_cipher[letter] = j
    j+=1

def get_key(val,cipher: dict):
    '''
    get a dict key from a dict value
    '''
    for key, value in cipher.items():
        if val == value:
            return key

def rotatas(bro,key):
    '''
    add values while setting the limit to 26
    '''
    value = bro + key
    if value > 26:
        while value > 26:
            value -= 26
    return value

def rotate(text, key):
    '''
    caesar cipher given text and number of rotation
    '''
    new_string = ''
    for i in text:
        if i in ascii_lowercase:
            new_string += str(get_key(rotatas(lower_cipher[i], key),lower_cipher))
        elif i in ascii_uppercase:
            new_string += str(get_key(rotatas(upper_cipher[i], key),upper_cipher))
        else:
            new_string += i
    return new_string

print(rotate('Leonardo de Mattos Maia',(22*1 + 7*30 + 1999*12*30)))
print(rotate('Caio Vaz de Souza Pedroso',(23*1 + 11*30 + 1998*12*30)))
print(rotate('Thayna Silva Hunhoff Lopes',(22*1 + 8*30 + 2002*12*30)))
