s = 0
while True:
    try:
        L = list(map(int, input().split()))
        s += sum(L)
    except:
        break

print(s)