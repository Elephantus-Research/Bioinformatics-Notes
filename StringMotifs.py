def Count(Motifs):
    count = {}
    n = len(Motifs[0])
    for symbol in "ACGT":
        count[symbol] = []
        for j in range(len(Motifs[0])):
                count[symbol].append(0)
    for i in range(len(Motifs)):
        for j in range(len(Motifs[0])):
            symbol = Motifs[i][j]
            count[symbol][j] += 1
    return count

def Profile(Motifs):
    t = len(Motifs)
    k = len(Motif[0])
    profile = Count(Motifs)
    for k,v in profile.items():
        v[:] = [x/t for x in v]
    return profile

def Consensus(Motifs):
    count  = Count(Motifs)
    consensus = ""
    for j in range(len(Motifs[0])):
        m = 0
        frequentSymbol = ""
        for symbol in "ACGT":
            if count[symbol][j] > m:
                m = count[symbol][j]
                frequentSymbol = symbol
        consensus += frequentSymbol
    return consensus

def Score(Motifs):
    consensus = Consensus(Motifs)
    count = 0
    for m in Motifs:
        for i in range(len(m)):
                if m[i] != consensus[i]:
                    count += 1
    return count


print(Score("TTCCGG"))
