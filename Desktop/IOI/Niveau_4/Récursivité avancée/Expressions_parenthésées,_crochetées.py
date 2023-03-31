from sys import stdin
ouverture = "([{<"
fermeture = ")]}>\n"
def bienParentheseeJusquA(fin):
   courant = stdin.read(1)
   if courant in fermeture:
      return courant == fin
   indice = ouverture.find( courant )
   if indice == -1 or bienParentheseeJusquA( fermeture[indice] ):
      return bienParentheseeJusquA( fin )
   return False
print("yes" if bienParentheseeJusquA("\n") else "no")