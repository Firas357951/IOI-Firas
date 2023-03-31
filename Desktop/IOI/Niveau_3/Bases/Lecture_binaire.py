Binaire = list(input())

n = len(Binaire)
s = 0
for idx in range(n):
    s += int(Binaire[n-1-idx]) * (2 ** idx)
print(s)