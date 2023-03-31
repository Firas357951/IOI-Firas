V = int(input())
n = int(input())
i = 0
for _ in range(n):
   if abs(V-int(input())) <= 50:
      i += 1
print(i)