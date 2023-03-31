tic = str(input()).upper()
Word_List = str(input()).split()

n = 0
for word in Word_List:
    if word.upper() == tic:
        n += 1
print(n)