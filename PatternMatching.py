import sys
input = sys.stdin.read().splitlines()
v_cholerae = input[1]

def PatternMatching(Pattern, Genome):
    output = list()
    for i in range(len(Genome)-len(Pattern)+1):
        if Pattern == Genome[i:i+len(Pattern)]:
            output.append(i)
    return output

Pattern = "CTTGATCAT"
Genome = "GATATATGCATATACTT"
print(PatternMatching(Pattern, "CTTGATCATCTTGATCATCTTGATCAT"))
