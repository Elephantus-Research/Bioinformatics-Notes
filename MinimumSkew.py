from SkewArray import SkewArray

def MinimumSkew(Genome):
    # generate an empty list position
    # set a variable equal to SkewArray(Genome)
    # find the minimun value of all values in the skew array
    # range over the length of the skew array and add all positions achieving the min to position
    arr = SkewArray(Genome)
    pos = []
    n = 0
    minarr = min(arr)
    for i in arr:
        if i == minarr:
            pos.append(n)
        n+=1
    return pos

Genome = "TAAAGACTGCCGAGAGGCCAACACGAGTGCTAGAACGAGGGGCGTAAACGCGGGTCCGAT"
print(MinimumSkew(Genome))









