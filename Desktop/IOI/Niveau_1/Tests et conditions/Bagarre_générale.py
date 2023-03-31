Arignon = int(input())
Evaran = int(input())
d = Evaran - Arignon
if abs(d)>10:
   if d > 0:
      print("La famille {} a un champ trop grand".format("Evaran"))
   else:
      print("La famille {} a un champ trop grand".format("Arignon"))