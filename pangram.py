'''
Determine if a sentence is a pangram. A pangram (Greek: παν γράμμα, pan gramma, "every letter") is a
sentence using every letter of the alphabet at least once. The best known English pangram is:

The quick brown fox jumps over the lazy dog.

The alphabet used consists of letters a to z, inclusive, and is case insensitive.
'''
alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

def is_pangram(sentence):
    '''
    function
    '''
    sentence_letters = []
    for char in sentence.lower():
        if char not in sentence_letters:
            if char.isalpha():
                sentence_letters.append(char)
    return sorted(sentence_letters) == alphabet