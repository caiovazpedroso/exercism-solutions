'''
Determine if a word or phrase is an isogram.
'''

def is_isogram(string):
    '''
    Checks for equal letters
    '''
    sorted_string = sorted(string.lower())
    i = 0
    while i < len(string)-1:
        if sorted_string[i] == '-' or sorted_string[i] == ' ':
            sorted_string[i] = ''
        if sorted_string[i] == sorted_string[i+1]:
            return False
        i += 1
    return True

print(is_isogram('rola cu he'))
