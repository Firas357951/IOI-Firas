L = str(input())
Code = str(input())

ch = ''
for letter in Code:
    if letter.isalpha():
        idx = ord(letter.lower()) - ord("a")
        if letter.isupper():    
            ch += L[idx].upper()
        else:
            ch += L[idx]
    else:
        ch += letter
print(ch)
