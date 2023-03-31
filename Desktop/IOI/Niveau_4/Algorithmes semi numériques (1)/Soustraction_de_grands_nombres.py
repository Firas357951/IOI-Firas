def subtract(B, a, b, r):
    result = (a-(b+r)) % B
    if a < (b+r):
        r = 1
    else:
        r = 0
    return (r, result)

def Compare(L1, N1, L2, N2):
    B = False
    if N2 > N1:
        B = True
    elif N2 == N1: 
        for idx in range(N1):
            if L1[N1-1-idx] < L2[N1-1-idx]:
                B = True
                break
            if L1[N1-1-idx] > L2[N1-1-idx]:
                break
                
    return B 

Base, N1, N2 = map(int, input().split()) 

N = max(N1, N2)
L1 = [0] * N
L2 = [0] * N
R = [0] * N

for idx, number in enumerate(input().split()):
    L1[N1-1 - idx] = int(number)
for idx, number in enumerate(input().split()):
    L2[N2-1 - idx] = int(number)    

B = Compare(L1, N1, L2, N2)
if B:
    L2, L1 = L1, L2

r = 0
for idx in range(N):
    r, result = subtract(Base, L1[idx], L2[idx], r)
    R[idx] = result
  
i = 0
for idx in range(N-1, -1, -1):
    if R[idx] != 0:
        i = idx
        break

if B:
    print("-", end= ' ')

for idx in range(i, -1, -1):
    print(R[idx], end= ' ')

