## Meilleur solution, Complexité N*ln(N)
N = int(input())
Prime = [True] * (N+1)
Prime[0] = 0

for number in range(2, N+1):
    if Prime[number]:
        M = 2
        product = M * number
        while product <= N:
            Prime[product] = False
            M +=1
            product = M * number

for idx, IsPrime in enumerate(Prime):
    if IsPrime:
        print(idx)

## Solution dont la compléxité N*sqrt(N)  
from math import sqrt
N = int(input())
def premier(n):
    B = True
    for i in range(2, int(sqrt(n))+1):
        if n % i == 0:
            B = False
            break
    return B
print(0)
print(1)
for i in range(2, N+1):
    if premier(i):
        print(i)















  