DNAbases = set('TCAGtcag')
RNAbases = set('UCAGucag')
def validate_base_sequence(base_seq, RNAflag=False):
    return set(base_seq) <= (RNAbases if RNAflag else DNAbases)


