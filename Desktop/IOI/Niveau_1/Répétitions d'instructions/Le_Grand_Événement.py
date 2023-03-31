from robot import *

for i in range(5):
   if i==0:
      
      for j in range(9):
         haut()
      droite()
      for j in range(8):
         bas()
      droite()      
   else:
      for j in range(8): 
         haut()   
      droite() 
      for j in range(8):
         bas()   
      if i<4:
         droite()
      
bas()

for i in range(9):
   gauche()  

