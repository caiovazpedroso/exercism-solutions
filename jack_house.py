'''
Recite the nursery rhyme 'This is the House that Jack Built'.
'''

verses = [
    'This is ',
    'the horse and the hound and the horn that belonged to ',
    'the farmer sowing his corn that kept ',
    'the rooster that crowed in the morn that woke ',
    'the priest all shaven and shorn that married ',
    'the man all tattered and torn that kissed ',
    'the maiden all forlorn that milked ',
    'the cow with the crumpled horn that tossed ',
    'the dog that worried ',
    'the cat that killed ',
    'the rat that ate ',
    'the malt ',
    'that lay in ',
    'the house that Jack built.',
    ]

def recitestr(start_verse, end_verse):
    '''
    recite as a string, not a list
    '''
    started = ''
    i = 0
    if start_verse == end_verse:
        if start_verse == 1:
            return verses[0] + verses[13]
        while i < start_verse:
            started = verses[12-i] + started
            i += 1
        return verses[0] + started + verses[13]

def recite(start_verse, end_verse):
    '''
    recite as a list
    '''
    started = ''
    i = 0
    if start_verse == end_verse:
        if start_verse == 1:
            return [verses[0] + verses[13]]
        while i < start_verse:
            started = verses[12-i] + started
            i += 1
        return [verses[0] + started + verses[13]]
    recital = []
    i = start_verse
    while i <= end_verse:
        recital.append(str(recitestr(i,i)))
        i += 1
    return recital

print(recite(1,6))
