N = int(input())
n = int(input())
B = False
for _ in range(n):
   if int(input()) == N:
      B = True

if B:
   print("Sorti de la ville")
else:
   print("Encore dans la ville")