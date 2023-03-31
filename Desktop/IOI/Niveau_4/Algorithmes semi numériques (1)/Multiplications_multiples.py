n = int(input())

def reste(int):
    return int % 10000

p = 1
for _ in range(n):
    p = reste(p)
    x = reste(int(input()))
    p *= x

print("{:04d}".format(p))





