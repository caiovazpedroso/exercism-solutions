import datetime
'''
Given a moment, determine the moment that would be after a gigasecond has passed.

A gigasecond is 10^9 (1,000,000,000) seconds.
'''

def add(moment):
    return moment + datetime.timedelta(seconds = 1000000000)

day = datetime.date(2021,4,25)
print(add(day))