n = int(input())
i = 1
while True:
   a = int(input())
   if a ==n : 
      print("Nombre d'essais nécessaires :")
      print(i)
      break 
   else:
      i+=1
      if a < n:
         print("c'est plus")
      if a > n:
         print("c'est moins")
         