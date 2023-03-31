xA, yA= map(int, input().split())
xB, yB = map(int, input().split())
xC, yC = map(int, input().split())

result = abs((xC-xA) * (yB-yA) - (yC-yA) * (xB-xA))
print(result)
