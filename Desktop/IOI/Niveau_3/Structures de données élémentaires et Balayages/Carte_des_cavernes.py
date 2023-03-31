N = int(input())
List = list(str(input()))
print(List)
print(len(List))
n = 0
idx = 0
while (n >= 0) and (idx <= (len(List)-1)):
    bracket = List[idx]
    if bracket == '(':
        n += 1
    elif bracket == ')':
        n -= 1
    idx += 1
    
if n == 0:
    print(1)
else:
    print(0)