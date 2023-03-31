import time


L = int(input())
D = int(input())
start = time.time()


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

end = time.time()
print(end - start)
























