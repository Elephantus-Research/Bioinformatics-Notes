def Complement(Pattern):
    dic = {'A': 'T', 'T':'A', 'C':'G', 'G':'C'}
    Pattern = Pattern.upper().rstrip()
    seq = ''
    for i in Pattern:
        seq += dic[i]
    return seq

def Reverse(Pattern):
    re = ""
    for i in range(1, len(Pattern)+1):
        re = re+Pattern[-i]
    return re


def ReverseComplement(Pattern):
    Pattern = Reverse(Pattern)
    Pattern = Complement(Pattern)
    return Pattern


print(ReverseComplement("AAAACCCGGT"))
