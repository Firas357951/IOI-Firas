import sys

NbC = int(input())
Cible = list(map(int, sys.stdin.readline().strip().split()))

NbL = int(input())
Lot = list(map(int, sys.stdin.readline().strip().split()))

idx = 0
for element in Cible:
    if idx < len(Lot):
       while Lot[idx] <= element:
          idx += 1
          if idx >= len(Lot):
             break
    print(Lot[idx-1], end =' ')
    
























