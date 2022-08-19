'''
Given a target word and a set of candidate words, this exercise requests
the anagram set: the subset of the candidates that are anagrams of the target.
'''
def split(word):
    return [char for char in word]

def find_anagrams(word, candidates):
    anagrams = []
    for cand in candidates:
        if cand.lower() == word or cand.upper() == word:
            continue
        if sorted(split(cand.upper())) == sorted(split(word.upper())):
            anagrams.append(cand)
    return anagrams

print(find_anagrams('LISTEN',['LISTEN','Silent']))