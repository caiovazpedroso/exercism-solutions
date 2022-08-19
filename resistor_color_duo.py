resistor_dict = {'black': 0, 'brown': 1, 'red': 2, 'orange': 3, 'yellow': 4,\
     'green': 5, 'blue': 6, 'violet': 7,'grey': 8, 'white': 9}
'''
function to transform resistor bands color to numerical values
'''
def value(colors):
    '''
    function
    '''
    # pylint: disable=unused-argument
    resistance = ''
    i = 0
    while i < 2:
          print(resistance)
          resistance += str(resistor_dict[colors[i]])
          i += 1
    return int(resistance)