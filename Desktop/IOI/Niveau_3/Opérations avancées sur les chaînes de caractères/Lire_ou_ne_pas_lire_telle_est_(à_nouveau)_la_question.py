N = int(input())

List = []
max = str(input())
print(max)
for _ in range(1, N):
    ch = str(input())
    if ch >= max:
        max = ch
        print(ch)    
    