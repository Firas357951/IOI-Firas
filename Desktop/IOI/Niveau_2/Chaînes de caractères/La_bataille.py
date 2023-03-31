w1 = str(input())
w2 = str(input())

n = min(len(w1), len(w2))

for idx in range(n):
   if w1[idx] > w2[idx]:
      print(2)
      print(idx)
      break
   if w1[idx] < w2[idx]:
      print(1)
      print(idx)
      break

if idx == n-1:
   if len(w1) > len(w2):
      print(1)
   elif len(w1) < len(w2):
      print(2)
   else:
      print("=")
      
   print(n)