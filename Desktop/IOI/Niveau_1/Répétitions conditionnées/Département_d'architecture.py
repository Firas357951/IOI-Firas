n = int(input())
if n != 0:
   a = 0 
   i = 0
   while True:
      if a + (i+1)*(i+1) >n:
         break
      else:
         i+=1
         a += i*i
   print(i)
   print(a)
else:
   print(0)
   print(0)
      