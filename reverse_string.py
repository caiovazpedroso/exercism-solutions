'''
pass
'''

def reverse(text):
    '''
    pass
    '''
    new_string = ''
    i = len(text) - 1
    while i >= 0:
        new_string += text[i]
        i -= 1
    return new_string

print(reverse('cool'))
