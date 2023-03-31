def binaire(n):
    return bin(n)[2:]

T = int(input())

Mult = []
for i in range(1, T+1):
    Mult.append([binaire(j * i) for j in range(1, T+1)])

for line in range(T):
    for col in range(T):
        print(Mult[line][col], end='\t')
    print()







