'''
function to convert a number to a string with raindrop sounds
'''

def convert(number):
    '''
    function to convert a number to a string with raindrop sounds
    '''
    rain_string = ''
    if number%3==0:
        rain_string+='Pling'
    if number%5==0:
        rain_string+='Plang'
    if number%7==0:
        rain_string+='Plong'
    if rain_string == '':
        rain_string = str(number)
    return rain_string
