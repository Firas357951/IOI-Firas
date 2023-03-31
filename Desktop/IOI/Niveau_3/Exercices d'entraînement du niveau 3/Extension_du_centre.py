## With Stacks
N1 = int(input())
L1 = list(map(int, input().split(' ')))
L1 = [L1[idx] for idx in range(N1-1, -1, -1)]

N2 = int(input())
L2 = list(map(int, input().split(' '))) 
L2 = [L2[idx] for idx in range(N2-1, -1, -1)]

L = []
while L1 != [] and L2 != []:
    if L1[-1] >= L2[-1]:
        L.append(L2.pop(-1))    
    else:
        L.append(L1.pop(-1)) 

if L1 == []:
    while L2 != []:
        L.append(L2.pop(-1))  
else:
    while L1 != []:
        L.append(L1.pop(-1))

for element in L:
    print(element, end= ' ')


## Simple method
N1 = int(input())
L1 = list(map(int, input().split(' ')))

N2 = int(input())
L2 = list(map(int, input().split(' ')))          

i = 0
j = 0
L = [None] * (N1+N2)
while i < N1 and j < N2:
    if L1[i] > L2[j]:
        L[i+j] = L2[j]
        j += 1
    else:
        L[i+j] = L1[i]
        i += 1
if i < N1:
    for idx in range(i, N1):
        L[idx+N2] = L1[idx]
else:
    for idx in range(j, N2):
        L[idx+N1] = L2[idx]

for element in L:
    print(element, end= ' ')