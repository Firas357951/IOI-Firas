Letter = str(input())
n = int(input())
i = 0

for _ in range(n):
   Line = str(input())
   for letter in Line:
      if letter == Letter:
         i += 1
print(i)   
