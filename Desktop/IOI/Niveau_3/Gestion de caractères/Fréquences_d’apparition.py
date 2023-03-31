ch = str(input())
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

for element in List:
    print(element/n)
