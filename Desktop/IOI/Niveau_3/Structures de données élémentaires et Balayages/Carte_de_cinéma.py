N = int(input())
Person_List = list(map(int, input().split()))

dict = {}
B = False
for person in Person_List:
    try:
        dict[person] += 1
        B = True
        break   
    except:
        dict[person] = 1
if B:
    print(person)
else:
    print(-1)

