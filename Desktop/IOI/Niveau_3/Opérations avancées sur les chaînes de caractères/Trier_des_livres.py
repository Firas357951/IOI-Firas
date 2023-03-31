N = int(input())

List = []
for _ in range(N):
    ch = str(input())
    List.append(ch)    
List.sort()

for ch in List:
    print(ch)