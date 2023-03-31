from math import sqrt

X, Y = map(int, input().split())

N = int(input())

def distance(x, y):
   return sqrt((X-x)**2 + (Y-y)**2)

Min = 20000
for _ in range(N):
   x, y = map(int, input().split())
   d = distance(x, y)
   if d < Min:
      Min = d
      Closest = (x, y)   
print(Closest[0], Closest[1])































