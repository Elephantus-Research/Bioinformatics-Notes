def SkewArray(Genome):
    skew = [1]
    for i in range(len(Genome)):
        if Genome[i] == 'C':
            skew.append(skew[i]-1)
        elif Genome[i] == 'G':
            skew.append(skew[i]+1)
        else:
            skew.append(skew[i])
    return skew

Genome = "CATTCCAGTACTTCGATGATGGCGTGAAGA"
print(SkewArray(Genome))
