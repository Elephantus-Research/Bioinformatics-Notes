from HammingDistance import HammingDistance
from ApproximatePatternMatching import ApproximatePatternMatching

def  ApproximatePatternCount(Pattern, Text, d):
    c = 0
    for i in range(len(Text)-len(Pattern)+1):
        if HammingDistance(Pattern,Text[i:i+len(Pattern)]) <=d:
            c +=1
    return c
