'''
Given a DNA strand, return its RNA complement (per RNA transcription).
'''

class NucleicAcid:
    '''
    pass
    '''
    def __init__(self, name, strand):
        '''
        pass
        '''
        self.name = name
        self.strand = strand.upper()
        #dna_to_rna = {'G': 'C', 'C': 'G', 'T': 'A', 'A': 'U'}

class DNA(NucleicAcid):
    '''
    pass
    '''
    def __init__(self,name,strand):
        self.complement = ''

    def complement(self):
        '''
        pass
        '''
        strand_complement = {'G': 'C', 'C': 'G', 'T': 'A', 'A': 'T'}
        dna_complement = ''
        for nuc in self.strand:
            dna_complement += strand_complement[nuc]
            print(dna_complement)
        return dna_complement

class RNA(NucleicAcid):
    '''
    pass
    '''

caioba = DNA('caioba', 'AGTAGTA')
caioba.complement

