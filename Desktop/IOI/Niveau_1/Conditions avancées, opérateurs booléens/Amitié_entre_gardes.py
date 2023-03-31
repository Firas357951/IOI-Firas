min_1 = int(input()) 
max_1 = int(input()) 

min_2 = int(input()) 
max_2 = int(input()) 

if (min_1 in range(min_2, max_2+1)) or (max_1 in range(min_2, max_2+1)) or \
   (min_2 in range(min_1, max_1+1)) or (max_2 in range(min_1, max_1+1)):
   print("Amis")
else:
   print("Pas amis")