min = int(input())
max = int(input())
i = 0

n = int(input())

for _ in range(n):
   if int(input()) in range(min, max+1):
      i += 1

print(i)