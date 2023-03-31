n = int(input())
i = 0
for _ in range(n):
   population = int(input())
   if population > 10000:
      i += 1
print(i)