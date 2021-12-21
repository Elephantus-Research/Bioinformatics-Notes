from PatternCount import PatternCount
def SymbolArray(Genome, symbol):
    arr = []
    n = len(Genome)
    ExtendedGenome = Genome + Genome[0:n//2]
    for i in range(n):
        arr[i] = PatternCount(ExtendedGenome[i:i+(n//2)], symbol)
        arr.append(arr[i])
    return arr

Genome = "AAAAAACCCC"
Symbol = "A"
print(SymbolArray(v_cholerae, Symbol))
