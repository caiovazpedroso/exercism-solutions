'''
Calculate the Hamming Distance between two DNA strands.
'''

def distance(strand_a, strand_b):
    '''
    pass
    '''
    if len(strand_a) != len(strand_b):
        raise ValueError("Strands must be of equal length.")
    hamming_dist = 0
    for i,j in zip(strand_a, strand_b):
        if i != j:
            hamming_dist += 1
    return hamming_dist
