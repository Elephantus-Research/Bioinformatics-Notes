def HammingDistance(p,q):
    c = 0
    for i, j in zip(p,q):
        if i != j:
            c+=1
    return c
