N, fileLength = map(int, input().split())

L = list(map(int, input().split()))

max = 0
file = []
s = 0

for element in L:
    s += element
    file.append(element)
    while (s > fileLength) and (file != []):
        s -= file.pop(0)
    a = len(file)
    if a > max:
        max = a 
        
print(max)        
































