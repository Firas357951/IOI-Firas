ch = str(input())
n = len(ch)

def frequence(ch):
    ch = ch.upper()
    List = [0] * 26
    n = 0
    words = ch.split()
    for word in words:
        for letter in word:
            if letter.isalpha():
                idx = ord(letter) - ord("A")
                List[idx] += 1
                n +=1
    max = 0
    if n > 0:
        for idx, element in enumerate(List):
            if element/n > max:
                max = element/n
                i = idx
        return i
    else:
        return 0

letter_num = frequence(ch)
D = letter_num - 4
txt = ''
for letter in ch:
    if letter.isupper():
        txt += chr(((ord(letter) - D) - 65) % 26 + 65)
    elif letter.islower():
        txt += chr(((ord(letter) - D) - 97) % 26 + 97)
    else:
        txt += letter
print(txt)

    




