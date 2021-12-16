def FrequencyMap(Text, k):
    freq = {}
    n = len(Text)
    for i in range(n-k+1):
        Pattern = Text[i:i+k]
        freq[Pattern] = 0
        if Pattern in freq:
            count = freq.get(Pattern)
            freq[Pattern] = count + 1
        else:
            freq[Pattern]  = 1
    return freq
Text = "CGCCTAAATAGCCTCGCGGAGCCTTATGTCATACTCGTCCT"
k = 3
def FrequencyMap2(Text, k):
    freq = {}
    n = len(Text)
    for i in range(n-k+1):
        Pattern = Text[i:i+k]
        freq[Pattern] = 0
        for j in range(n-k+1):
            if Pattern == Text[j:j+k]:
                freq[Pattern] +=1
    return freq

print(FrequencyMap2(Text,k))
