i = 0
while True:
   mdps = int(input("Entrez le code :"))
   print()
   if mdps == 4242:
      if i == 0:
         i +=1
         print("Encore une fois.")
      else:
         print("Bravo.")
         break