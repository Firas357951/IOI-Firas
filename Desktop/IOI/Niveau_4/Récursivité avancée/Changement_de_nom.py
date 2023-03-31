N = int(input())
ch = input()
n = int(input())

def Write(word, n):
    if n == 0:
        print(word)
    else:
        for letter in ch:
            Write(word + letter, n-1)

print(N**n)        
Write('', n)