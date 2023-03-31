N = int(input())

List = [None] * N
for idx in range(N):
    french, english = str(input()).split()
    List[idx] = english + ' '+ french
List.sort()
for ch in List:
    print(ch)




