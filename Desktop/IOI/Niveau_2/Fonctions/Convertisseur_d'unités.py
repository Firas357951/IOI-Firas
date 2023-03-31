n = int(input())

def pied(x):
   return str(x / 0.3048) + ' p'

def livre(x):
   return str(x * 0.002205) + ' l'
   
def f(x):
   return str(x * 1.8 + 32) + ' f'

for _ in range(n):
   Line = str(input())
   v, unity = Line.split(' ')
   if unity == 'm':
      print(pied(float(v)))
   if unity == 'g':
      print(livre(float(v)))
   if unity == 'c':
      print(f(float(v)))