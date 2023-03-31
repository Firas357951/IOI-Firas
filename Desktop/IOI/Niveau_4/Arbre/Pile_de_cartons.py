def f(L, j):
    if L[j] == []:
        pass
    
    else:
        List = L[j].copy()
        for i in List:
            print("A", i)
            L[j].pop(0)
            f(L, i)
            print("R", i)
            
            
from sys import stdin
nbCartons = int(input())
posesDessus= [None]*(nbCartons + 1)
for carton,cartons in zip(range(nbCartons + 1),stdin):
    posesDessus[carton] = \
        [int(carton) for n,carton in enumerate(cartons.split()) if n > 0]
L =  posesDessus
f(L, 0)