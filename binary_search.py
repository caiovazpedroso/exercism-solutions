'''
Implement a binary search algorithm.
Searching a sorted collection is a common task. A dictionary is a sorted list
of word definitions. Given a word, one can find its definition. A telephone book
is a sorted list of people's names, addresses, and telephone numbers.
Knowing someone's name allows one to quickly find their telephone number and address.
'''


def find(search_list, value):
    if value not in search_list:
        raise ValueError('value not in array')
    left, right, thingy = 0, search_list[-1], 0
    while thingy != value:
        thingy = round((left + right)/2)
        print(left, right)
        if thingy == value:
            return search_list.index(thingy)
        elif thingy > value:
            right = thingy - 1
        elif thingy < value:
            left = thingy + 1

listeca = [i for i in range(1,100)]
listuca = [i for i in range(10,45,2)]
print(find(listeca,49))
print(listuca)
print(find(listuca,32))