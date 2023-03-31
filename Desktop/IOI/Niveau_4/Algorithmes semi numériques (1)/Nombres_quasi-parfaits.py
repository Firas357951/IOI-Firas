## Meilleur solution trouvée, la complexité est N*ln(N)
## on inverse la logique et on calcul pour chaque diviseur ces multiples
L = int(input())
D = int(input())

S = [1] * (L+1)
S[1] = 0
S[0] = 0 
for diviseur in range(2, L):
    j = 2
    produit = diviseur * j
    while produit <= L:
        S[produit] += diviseur
        j +=1
        produit = diviseur * j

number = 0
for idx in range(1, L+1):
    if abs(S[idx]-idx) <= D:
        number += 1
print(number)

## Solution dont la complexité est difficile à calculer mais bien meilleur que N*sqrt(N)
## On determine la factorisation en nombre premier du nombre n pour calculer s(n)
from math import sqrt 

def add(element, dict):
    try:
        dict[element] += 1 
    except:
        dict[element] = 1
        
def diviseur(n):
    dict = {}
    while n > 1:
        B = False
        idx = int(sqrt(n))
        for i in range(2, idx + 1): 
            if n % i == 0:
                B = True
                n = n // i
                add(i, dict)
                break
        if not(B):
            add(n, dict)
            break 
    return dict   

def s_prime(p, k):
    return int((1 - p**(k+1)) / (1-p))

def sum(n):
    divList = diviseur(n)
    p = 1
    for prime in divList:
        p *= s_prime(prime, divList[prime])  
    return p - n    

L = int(input())
D = int(input())
memo = [0] * (L+1)

for i in range(2, L+1):
    if memo[i] != 0:
        s = memo[i]
    else:
        s = sum(i)
        if s == 1:
            p0 = i
            idx = 1
            while p0 <= L:
                Sp0 = s_prime(i, idx-1)
                for j in range(1, i):
                    p = p0 * j
                    if p > L :
                        break
                    else:
                        memo[p] = Sp0*memo[j] + p0*memo[j] + j*Sp0
                idx += 1
                p0 = i ** idx 
        else:
            memo[i] = s
number = 0
for idx in range(1, L+1):
    if abs(memo[idx] - idx) <= D:
        number += 1
print(number)


## Solution dont la complexité est meilleur que N*sqrt(N) 
from math import sqrt

def somme_diviseur(n):
    s = 1
    idx = int(sqrt(n))
    for i in range(2, idx + 1):
        if n % i == 0:
            if n // i != i:
                s += i + n // i
            else:
                s += i
    return s
def somme_premier(p, k):
    return int((1 - p**k) / (1-p))
    
L = int(input())
D = int(input())
memo = [0] * (L+1)
for i in range(2, L+1):
    if memo[i] != 0:
        s = memo[i]
    else:
        s = somme_diviseur(i)
        if s == 1:
            p0 = i
            idx = 1
            while p0 <= L:
                Sp0 = somme_premier(i, idx)
                for j in range(1, i):
                    p = p0 * j
                    if p > L :
                        break
                    else:
                        memo[p] = Sp0*memo[j] + p0*memo[j] + j*Sp0
                idx += 1
                p0 = i ** idx 
        else:
            memo[i] = s
number = 0
for idx in range(1, L+1):
    if abs(memo[idx] - idx) <= D:
        number += 1
print(number)

    