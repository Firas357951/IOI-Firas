N = int(input())

S = [[' '] * N for _ in range(N)]
def f(N, i, j):
    if N == 1:
        S[i][j] = '#'
    else:
        f(N//2, i, j)
        f(N//2, i + N//2, j)
        f(N//2, i, j + N//2)

f(N, 0, 0)
for line in range(N):
    for col in range(N):
        print(S[line][col], end='')
    print()