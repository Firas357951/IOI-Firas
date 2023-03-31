N = int(input()) 

def key(n):
    if n % 2 == 0:
        return 3 * n
    else:
        return - 5 * n
        
for idx in range(2, N+1):
    D = key(idx)
    ch = str(input())
    txt = ''
    for letter in ch:
        if letter.isupper():
            txt += chr(((ord(letter) - D) - 65) % 26 + 65)
        elif letter.islower():
            txt += chr(((ord(letter) - D) - 97) % 26 + 97)
        else:
            txt += letter
    print(txt)