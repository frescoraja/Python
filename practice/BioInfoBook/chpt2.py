from random import randint as rand

def random_base(RNAflag=False):
    return ('UCAG' if RNAflag else 'TCAG')[rand(0,3)]

def random_codon(RNAflag=False):
    return random_base(RNGflag) + random_base(RNAflag) + random_base(RNAflag)

def replace_base_randomly_using_names(base_seq):
    """Return a sequence with a base at a randomly selected position of base_seq
    replaced by a base chosen randomly from the three bases that are not at that
    position"""
    position = rand(0, len(base_seq) - 1 )
    base = base_seq[position]
    bases = 'TCAG'
    bases.replace(base, '')
    newbase = bases[rand(0, 2)]
    beginning = base_seq[0:position]
    end = base_seq[position+1:]
    return beginning + newbase + end

def replace_base_randomly_using_expression(base_seq):
    position = rand(0, len(base_seq) - 1)
    return (base_seq[0:position] + \
            'TCAG'.replace(base_seq[position], '')[rand(0, 2)] + \
            base_seq[position+1:])

def replace_base_randomly(base_seq):
    position = rand(0, len(base_seq) - 1)
    bases = 'TCAG'.replace(base_seq[position], '')
    return (base_seq[0:position] + bases[rand(0,2)] + base_seq[position+1:])

def validate_base_sequence(base_sequence, RNAflag=False):
    """Return True if the base_sequence contains only upper- or lowercase T (or
    U, if RNAflag), C, A, G characters, otherwise False"""
    seq = base_sequence.upper()
    return len(seq) == (seq.count('U' if RNAflag else 'T') +
            seq.count('C') + seq.count('A') + seq.count('G'))

def gc_content(base_seq):
    """Return percentage of G and C characters in base_seq"""
    assert validate_base_sequence(base_seq), \
            'argument has invalid characters'
    seq = base_seq.upper()
    return (seq.count('G') + seq.count('C')) / float(len(seq))

def recognition_site(base_seq, recognition_seq):
    """Return the first position in base_seq where recognition_seq occurs, or -1
    if not found"""
    return base_seq.find(recognition_seq)

def test():
    assert validate_base_sequence('ACGT')
    assert validate_base_sequence('')
    assert not validate_base_sequence('ACUG')

    assert validate_base_sequence('ACUG', True)
    assert not validate_base_sequence('ACUG', False)
    assert validate_base_sequence('ACUG', True)

    assert 0.5 == gc_content('ACTG')
    assert 1.0 == gc_content('CCGG')
    assert .25 == gc_content('ACTT')

    print('All tests passed.')

test()

