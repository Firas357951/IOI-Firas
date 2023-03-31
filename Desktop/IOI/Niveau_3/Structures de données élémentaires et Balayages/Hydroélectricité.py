K, N = map(int, input().split())
List = list(map(int, input().split()))

s = 0
for idx in range(K):
    s += List[idx]
max = s

for idx in range(K, N):
    s += List[idx]
    s -= List[idx - K]
    if s > max:
        max = s
print(max)