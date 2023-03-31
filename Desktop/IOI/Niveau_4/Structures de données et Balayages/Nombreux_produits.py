import sys

NbDistrib = int(input())
NbOperation = int(input())

file = []
for _ in range(NbDistrib):
    file.append([])
    
for _ in range(NbOperation):
    Nb, n, date = map(int, sys.stdin.readline().strip().split()) 
    if date != 0:
        file[Nb-1].extend([date] * n)
    else:
        file[Nb-1] = file[Nb-1][-n:]
        
    
for idx in range(NbDistrib):
    if len(file[idx]) == 0: 
        print(0)
    else:
        print(min(file[idx]))




























