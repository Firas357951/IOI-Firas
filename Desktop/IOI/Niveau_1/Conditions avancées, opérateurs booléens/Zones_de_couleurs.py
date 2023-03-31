def Zone_Rouge(x, y):
   if ((x > 15) and (x < 45)) or ((x > 60) and (x < 85)):
      if (y > 60) and (y < 70):
         return True
   return False
   
def Zone_Jaune(x, y):
   if ((x > 0) and (x < 10)):
      return True
   if ((y > 0) and (y < 10)): 
      return True
   if ((x > 85) and (x < 90)):
      return True
   if ((y > 55) and (y < 70)):
      return True
   if ((x > 25) and (x < 50)):
      if (y > 20) and (y < 45):
         return True
   return False

def Dehors(x, y):
   if x < 0 or x > 90:
      return True
   if y < 0 or y > 70:
      return True
   return False
   
n = int(input())

for _ in range(n):
   x = int(input())
   y = int(input())
   if Dehors(x, y):
      print("En dehors de la feuille")
   elif Zone_Rouge(x, y):
      print("Dans une zone rouge")
   elif Zone_Jaune(x, y):
      print("Dans une zone jaune")
   else:
      print("Dans une zone bleue")
