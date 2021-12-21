from HammingDistance import HammingDistance

def ApproximatePatternMatching(Text, Pattern, d):
    pos = []
    for i in range(len(Text)-len(Pattern)+1):
        if HammingDistance(Text[i:i+len(Pattern)], Pattern) <= d:
            pos.append(i)
    return pos

Pattern = "ATTCTGGA"
Text = "CGCCCGAATCCAGAACGCATTCCCATATTTCGGGACCACTGGCCTCCACGGTACGGACGTCAATCAAAT"
d = 3
print(ApproximatePatternMatching(Text, Pattern, d))

