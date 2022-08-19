'''
Convert a phrase to its acronym.

Techies love their TLA (Three Letter Acronyms)!

Help generate some jargon by writing a program that converts
a long name like Portable Network Graphics to its acronym (PNG).

Punctuation is handled as follows: hyphens are word separators
(like whitespace); all other punctuation can be removed from the input.
'''

from string import ascii_lowercase, ascii_uppercase

def abbreviate(words: str):
    '''
    Convert a phrase to its acronym.
    '''
    i = 0
    acro = ''
    while i < len(words):
        if words[i] not in ascii_lowercase and words[i] not in ascii_uppercase:
            words = words[:i] + ' ' + words[i+1:]
            if words[i] == words[i-1]:
                words = words[:i-1] + words[i:]
                i -= 1
        i += 1
    for i in words.split(' '):
        if i != 's':
            acro += (list(i))[0]
    return acro.upper()

print(abbreviate('Liquid-crystal display'))
print(abbreviate('Something - I made up from thin air'))
print(abbreviate('First in, First out'))
print(abbreviate("Halley's Comet"))
