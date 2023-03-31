N = int(input())

def f(N, i, j):
    if N == 1:
        print(i, '->', j)
    else:
        k = [1, 2, 3]
        k.remove(i)
        k.remove(j)
        k = k[0]
        f(N-1, i, k)
        f(1, i, j)
        f(N-1, k, j)

f(N, 1, 3)
        
        
