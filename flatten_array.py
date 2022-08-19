'''
Take a nested list and return a single flattened list with all values except nil/null.

The challenge is to write a function that accepts an arbitrarily-deep nested list-like structure and returns a flattened structure without any nil/null values.

For Example

input: [1,[2,3,null,4],[null],5]

output: [1,2,3,4,5]
'''

def flatten(iterable):
    '''
    pass
    '''
    flattened = []
    for item in iterable:
        print(item)
        if item == None:
            continue
        if isinstance(item,list):
            print('yes', flattened)
            flattened += flatten(item)
            print('go',flattened)
        else:
            flattened.append(item)
            print(flattened)
    return flattened

print(flatten([1,[2,None,[None,1,[90,None,75]]],4,5]))