'''
Given a DNA strand, return its RNA complement (per RNA transcription).
'''
transcription = {'G': 'C', 'C': 'G', 'T': 'A', 'A': 'U'}

def to_rna(dna_strand):
    '''
    pass
    '''
    rna_strand = ''
    for nucleotide in dna_strand:
        rna_strand += transcription[nucleotide]
    return rna_strand