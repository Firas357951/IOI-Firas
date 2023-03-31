n = int(input())
s1 = 0
s2 = 0
for _ in range(n):
   s1 += int(input())
   s2 += int(input())

if s1 > s2:
   print("L'équipe 1 a un avantage")
if s1 < s2:
   print("L'équipe 2 a un avantage")
   
print("Poids total pour l'équipe 1 : {}".format(s1))
print("Poids total pour l'équipe 2 : {}".format(s2))