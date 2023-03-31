## Problème avec la  pile de la récursivité elle dépasse 1000
N = int(input())
I = input().split(' ')
I = [int(i) for i in I]
max = 0
dict = {}
def f(N):
    if N == 0:
        return 0 
    else:
        try:
            return dict[N]
        except:
            X = f(I[N-1]) + 1 
            dict[N] = X
            return X
for i in range(1, N + 1):
    x = f(i)
    if x > max:
        max = x
print(max)

# # Solution  

# # from sys import setrecursionlimit
# # setrecursionlimit(50 * 1000)

# # def main():
# #    nbProduits = int(input())
# #    contenus = [[] for _ in range(nbProduits + 1)]
# #    for contenu, contenant in enumerate(map(int, input().split()), 1):
# #       contenus[contenant].append(contenu)
# #    def hauteur(racine):
# #       if racine:
# #          return max([hauteur(contenus[produit]) for produit in racine]) + 1
# #       return 0
# #    print(hauteur(contenus[0]))
# # main()




     
  
    