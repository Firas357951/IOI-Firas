I, L = map(int, input().split())

def hcf(a, b):
    if(b == 0):
        return a
    else:
        return hcf(b, a % b)
        
result = (I*L) // hcf(I, L)        
print(result)











