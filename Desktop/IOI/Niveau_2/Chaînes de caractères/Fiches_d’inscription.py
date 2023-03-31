n = int(input())

for _ in range(n):
   ch = str(input())
   prenom, nom = ch.split(" ")
   print("{} {}".format(nom, prenom))