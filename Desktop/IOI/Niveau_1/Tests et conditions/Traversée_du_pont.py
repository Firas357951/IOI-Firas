n = int(input())
m = int(input())
if n + m >= 10:
   print("Taxe spéciale !")
   print(36)
else:
   print("Taxe régulière")
   print(2*(n+m))