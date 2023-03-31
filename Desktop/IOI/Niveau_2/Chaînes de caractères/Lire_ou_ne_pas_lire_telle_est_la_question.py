n = int(input())
max = 0
for _ in range(n):
   title = str(input())
   if len(title) > max:
      print(title)
      max = len(title)