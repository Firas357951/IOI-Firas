n = int(input())
max = int(input())

for _ in range(n):
   title = str(input())
   resume = str(input())
   if len(resume) < max:
      print(title) 