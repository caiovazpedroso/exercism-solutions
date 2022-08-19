'''
Your task in this exercise is to write code that returns the lyrics of the song:
"The Twelve Days of Christmas."
'''

days = ['first','second','third','fourth','fifth','sixth','seventh','eighth','ninth','tenth','eleventh','twelfth']
verse = [' twelve Drummers Drumming,',' eleven Pipers Piping,',' ten Lords-a-Leaping,',' nine Ladies Dancing,',' eight Maids-a-Milking,',\
' seven Swans-a-Swimming,',' six Geese-a-Laying,',' five Gold Rings,',' four Calling Birds,',' three French Hens,',' two Turtle Doves,',' a Partridge in a Pear Tree']
#On the {days[end_verse-1]} day of Ch
def recite(start_verse, end_verse):
    '''
    sings
    '''
    song = ''
    if end_verse == start_verse:
        song = f'On the {days[end_verse-start_verse]} day of Christmas my true love gave to me:{verse[12 - start_verse]}.'
    else:
        thing = ''
        i = 0
        while i < (end_verse - start_verse):
            print(start_verse + i - 1)
            thing += verse[(12 - end_verse) + start_verse + i - 1]
            i += 1
        song = f'On the {days[end_verse-start_verse]} day of Christmas my true love gave to me:{thing} and{verse[12 - start_verse]}.'
    if song[-2] == ',':
        final_song = song[0:-2] + '.'
    else:
        final_song = song
    return [final_song]

print(recite(2,2))
