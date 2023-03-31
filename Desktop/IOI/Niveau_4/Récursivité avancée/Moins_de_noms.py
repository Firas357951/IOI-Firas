N = int(input())
ch = input()
n = int(input())

def Write(word, n):
    if n == 0:
        print(word)
    else:
        for letter in [l for l in ch if l not in word]:
            Write(word + letter, n-1)

p = 1 
for number in range(N-n+1, N+1):
    p *= number
print(p)
Write('', n)