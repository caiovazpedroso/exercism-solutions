'''
pass
'''
def leap_year(year):
    '''
    pass
    '''
    if year%4 == 0:
        if year%100 == 0:
            if year %400 == 0:
                return True
            return False
        return True
    return False

print(leap_year(1))
