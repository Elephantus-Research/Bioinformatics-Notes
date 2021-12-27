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
    k = len(Motifs[0])
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

def PrCompute(Motif, profile):
    c = 1
    for i in range(len(Motif)-1):
        for nucleotide in profile:
            if Motif[i]==nucleotide:
                c*=profile[nucleotide][i]
    return c

def Pr(Text, Profile):
    p = 1
    for i in range(len(Text)):
        p = p*Profile[Text[i]][i]
    return p

def PrMostProbableKmer(text,k,profile):
    pr = {}
    mpk =[]
    for i in range(len(text)-k+1):
        kmer=text[i:i+k]
        pro = Pr(kmer, profile)
        pr[kmer] = pro
    m = max(pr.values())
    for k,v in pr.items():
        if pr[k] == m:
            mpk.append(k)
    return mpk[0]

def GreedyMotifSearch(Dna,k,t):
    best_motifs = []
    for i in range(0,t):
        best_motifs.append(Dna[i][0:k])
    n = len(Dna[0])
    for m in range(n-k+1):
        Motifs=[]
        Motifs.append(Dna[i][0:k])
        for j in range(i,t):
            p = Profile(Motifs[0:j])
            Motifs.append(PrMostProbableKmer(Dna[j],k,p))
        if Score(Motifs) < Score(best_motifs):
            best_motifs = Motifs
    return best_motifs

Dna = [
"GGCGTTCAGGCA",
"AAGAATCAGTCA",
"CAAGGAGTTCGC",
"CACGTCAATCAC",
"CAATAATATTCG"
]
Motif = "TCGTGGATTTCC" 
profile = {
    'A': [0.2, 0.2, 0.0, 0.0, 0.0, 0.0, 0.9, 0.1, 0.1, 0.1, 0.3, 0.0],
    'C': [0.1, 0.6, 0.0, 0.0, 0.0, 0.0, 0.0, 0.4, 0.1, 0.2, 0.4, 0.6],
    'T': [0.7, 0.2, 0.0, 0.0, 0.1, 0.1, 0.0, 0.5, 0.8, 0.7, 0.3, 0.4]
}

Text= "TCGGTA"
print(Pr(Text, profile_2))
print(GreedyMotifSearch(Dna, 3, 5))
