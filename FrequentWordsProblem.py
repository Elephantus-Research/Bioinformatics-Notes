Text = "GATCCAGATCCCCATAC"
dictionary = {}
for i in range(len(Text)-2+1):
    curr = Text[i:i+2]
    print(curr)
    if curr in dictionary:
        count = dictionary.get(curr)
        dictionary[curr] = count +1
    else:
        dictionary[curr] = 1
print(dictionary)
