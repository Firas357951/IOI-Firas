import sys

N = int(input())
L = []
for _ in range(N):
    ch = sys.stdin.readline().strip()
    for idx, letter in enumerate(ch):
        if letter == 'O':
            L.append(chr(65+idx))

print(''.join(L))
