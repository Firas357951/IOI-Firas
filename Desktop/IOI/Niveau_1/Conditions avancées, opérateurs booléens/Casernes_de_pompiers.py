n = int(input())

def intersection(min, max, a, b):
   if (a >= max) or (b <= min):
      return False
   return True 

for _ in range(n):
   min_x1 = int(input())
   max_x1 = int(input())
   min_y1 = int(input())
   max_y1 = int(input())
   
   min_x2 = int(input())
   max_x2 = int(input())
   min_y2 = int(input())
   max_y2 = int(input())
   
   if intersection(min_x1, max_x1, min_x2, max_x2) and intersection(min_y1, max_y1, min_y2, max_y2):
      print("OUI")
   else:
      print("NON")