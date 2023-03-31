N = int(input())
P = int(input())

def factorial(n):
    p = 1
    for i in range(2, n+1):
        p *= i
    return p

result = int(factorial(N)/(factorial(N-P)))
print(result)


