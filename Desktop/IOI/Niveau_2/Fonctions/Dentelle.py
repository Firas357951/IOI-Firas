n = int(input())

def write(n, symbol):
   for _ in range(n):
      print(symbol, end= '')
   print()
   
write(n, "X")
write(n, "#")
write(n, "i")