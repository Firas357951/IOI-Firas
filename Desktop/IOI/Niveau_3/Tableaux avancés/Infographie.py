Ligne, Col = map(int, input().split())

N = int(input())
L = [None] * Ligne
for idx in range(Ligne):
    L[idx] = ["."] * Col

for _ in range(N):
    List = str(input()).split()
    symbol = List.pop(-1)
    iL1, iC1, iL2, iC2 = [int(i) for i in List]
    for i in range(iL1, iL2 + 1):
        for j in range(iC1, iC2 + 1):
            L[i][j] = symbol
        
for ligne in range(Ligne):
    for col in range(Col):
        print(L[ligne][col], end= '')
    print()














