def Wait(mdps, trial):
   B = False
   if mdps != trial:
      print("Entrez le code :")
   else:
      B = True
   return B
   
B = False
print("Entrez le code :")
while not(B):
   trial = int(input())
   B = Wait(4242, trial)
   
print("Premier code bon.")
print("Entrez le code :")
B = False
while not(B):
   trial = int(input())
   B = Wait(2121, trial)   
print("Bravo.")