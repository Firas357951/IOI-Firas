N = int(input())
pile = []
for _ in range(N):
    q, date = map(int, input().split())
    if q > 0:
        for _ in range(q):
            pile.append(date)
    else:
        for _ in range(-q):
            pile.pop(-1)

print(min(pile))
