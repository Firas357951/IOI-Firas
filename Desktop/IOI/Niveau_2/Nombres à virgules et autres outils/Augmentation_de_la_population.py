from math import floor

n = int(input())
r = float(input())

result = floor(n * (1 + r/100))
print(result)