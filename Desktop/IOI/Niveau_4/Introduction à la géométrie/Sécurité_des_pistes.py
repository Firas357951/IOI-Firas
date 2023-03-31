xA, yA, xB, yB = map(int, input().split())
xC, yC, xD, yD = map(int, input().split())

a = xB - xA
b = yB - yA
c = xD - xC
d = yD - yC

det = b*c - a*d
k1 = ((xA-xC) * d + (yC-yA) * c) / det
k2 = ((xA-xC) * b + (yC-yA) * a) / det
x = k1 * a + xA
y = k1 * b + yA

print(x, y)