ch = input()

i = 0
ind = '   '
for letter in ch:
    if letter == '{':
        print(ind * i + letter)
        i += 1
    else:
        i -= 1
        print(ind * i + letter)