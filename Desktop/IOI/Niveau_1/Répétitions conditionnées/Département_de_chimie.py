n = int(input())
min = int(input())
max = int(input())
for i in range(n):
   t = int(input())
   if t<=max and t>=min:
      print("Rien à signaler")
   else:
      print("Alerte !!")
      break