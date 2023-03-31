D = int(input())
dict = [None] * D
for idx in range(D):
    dict[idx] = input()
    
N = int(input())
possibility = []
L = list(input())
for word in dict:
    for letter in L: 
        if word[0] == letter:
            possibility.append(word)

idx = 0           
while idx < len(possibility):
    word = possibility[idx]
    idx += 1
    if len(word) != N:
       possibility.remove(word)
       idx -= 1   
     
for idx in range(1, N):
    L = list(input())
    i = 0
    while i < len(possibility):
        word = possibility[i]
        i += 1
        B = False
        for letter in L:
           if word[idx] == letter:
               B = True
               break
        if not(B):
           i -= 1
           possibility.remove(word)  
                     
print(possibility[0])