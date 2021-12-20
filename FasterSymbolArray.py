from PatternCount import PatternCount

def FasterSymbolArray(Genome, symbol):
    arr = {}
    n = len(Genome)
    ExtendedGenome = Genome + Genome[0:n//2]
    # Look at the first half of Genome to compute first array value
    arr[0] = PatternCount(Genome[0:n//2], symbol)

    for i in range(1, n):
        # start by setting the current array value equal to the previous array value
        arr[i] = arr[i-1]

        # the current array value can differ from the previous array value by at most 1
        if ExtendedGenome[i-1] == symbol:
            arr[i] = arr[i]-1
        if ExtendedGenome[i+(n//2)-1] == symbol:
            arr[i] = arr[i]+1
    return arr

Genome = "AAAAGGGG"
symbol = "A"
print(FasterSymbolArray(Genome, symbol))
