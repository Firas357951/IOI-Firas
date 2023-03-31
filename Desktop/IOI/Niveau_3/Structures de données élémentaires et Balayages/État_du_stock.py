N = int(input())
L = list(map(int, input().split()))
n = int(input())
for _ in range(n):
    idx, quantity = map(int, input().split())
    L[idx - 1] += quantity

for element in L:
    print(element, end=' ')
