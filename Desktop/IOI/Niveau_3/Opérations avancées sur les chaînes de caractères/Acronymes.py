Acronym = str(input()).upper()
N = int(input())
for _ in range(N):
    Words = str(input()).upper().split()
    if len(Words) == len(Acronym):
        B = True
        for idx, word in enumerate(Words):
            if word[0] != Acronym[idx]:
                B = False
                break
        if B:
            for word in Words:
                word1 = list(word.lower())
                word1[0] = word[0].upper() 
                print("".join(word1), end=' ')
            print()
