'''
pass
'''
color_dict = {
    'black': 0, 'brown': 1, 'red': 2, 'orange': 3, 'yellow': 4, 'green': 5,\
    'blue': 6, 'violet': 7, 'grey': 8, 'white': 9
}

def color_code(color):
    '''
    pass
    '''
    return color_dict[color]

def colors():
    '''
    pass
    '''
    color_list = []
    for key in color_dict:
        color_list.append(key)
    return color_list

print(colors())
print(color_code('grey'))
