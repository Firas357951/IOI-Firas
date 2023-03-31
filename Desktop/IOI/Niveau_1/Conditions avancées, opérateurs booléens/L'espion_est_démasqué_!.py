n = int(input())

for _ in range(n):
   s = 0
   taille = int(input())
   age = int(input())
   poids = int(input())
   cheval = int(input())
   cheveux = int(input())
   
   if taille in range(178, 183):
      s += 1
   if age >= 34:
      s += 1
   if poids < 70:
      s += 1
   if cheval == 0:
      s += 1
   if cheveux == 1:
      s += 1
   
   if s == 5:
      print("Très probable")
   elif s >= 3:
      print("Probable")
   elif s == 0:
      print("Impossible")
   else:
      print("Peu probable")