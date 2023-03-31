from robot import *

for idx in range(1, 11):
   for _ in range(idx):
      droite()
   ramasser()
   for _ in range(idx):
      gauche()
   deposer()