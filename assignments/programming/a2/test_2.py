#original file name in coursera a2.py
def get_length(dna):
    """ (str) -> int

    Return the length of the DNA sequence dna.

    >>> get_length('ATCGAT')
    6
    >>> get_length('ATCG')
    4
    """
    return len(dna)

def is_longer(dna1, dna2):

    """ (str, str) -> bool

    Return True if and only if DNA sequence dna1 is longer than DNA sequence
    dna2.

    >>> is_longer('ATCG', 'AT')
    True
    >>> is_longer('ATCG', 'ATCGGA')
    False
    """
    return dna1 > dna2

def count_nucleotides(dna, nucleotide):
    """ (str, str) -> int

    Return the number of occurrences of nucleotide in the DNA sequence dna.

    >>> count_nucleotides('ATCGGC', 'G')
    2
    >>> count_nucleotides('ATCTA', 'G')
    0
    """
    return dna.count(nucleotide)

def contains_sequence(dna1, dna2):
    """ (str, str) -> bool

    Return True if and only if DNA sequence dna2 occurs in the DNA sequence
    dna1.

    >>> contains_sequence('ATCGGC', 'GG')
    True
    >>> contains_sequence('ATCGGC', 'GT')
    False

    """
    return dna2 in dna1

def is_valid_sequence(dna):
    #’A’, ’T’, ’C’ y ’G’
    
    for i in dna:
        if i != 'A' and i != 'T' and i != 'C' and i != 'G':
            return False

    return True

def insert_sequence(dna1, dna2, index):
    return dna1[:index] + dna2 + dna1[index:]

def get_complement(nucleotide):
    #El ADN tiene 2 hebras en una doble hélice. Los nucleótidos de una hebra están unidos a los nucleótidos de la otra hebra. 
    #A y T se pueden unir y, por lo tanto, se complementan entre sí; De manera similar, C y G son complementarios entre sí.
    #
    if nucleotide == 'A' or nucleotide == 'T':
        if nucleotide == 'A':
            return 'T'
        return 'A'

    elif nucleotide == 'C' or nucleotide == 'G':
        if nucleotide == 'C':
            return 'G'
        return 'C'

def get_complementary_sequence(dna):
    cdna = ''
    for i in dna:
        cdna += get_complement(i)

    return cdna
