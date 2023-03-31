N = int(input())
List = list(map(int, input().split(' ')))

dict = {}
for element in List:
    if element in dict:
        dict[element] += 1
    else:
        dict[element] = 1

print(max(list(dict.values())))
