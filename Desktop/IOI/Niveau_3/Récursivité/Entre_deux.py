N, M = map(int, input().split())

def f(M):
    if M == N:
        print(N, end=' ')
    else:
        print(M, end=' ')
        f(M-1)
        
        
f(M)