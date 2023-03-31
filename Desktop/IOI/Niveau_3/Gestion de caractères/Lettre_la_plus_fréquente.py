ch = str(input())
dict = {}
for i in ch:
    if i != ' ':
        try:
            dict[i.upper()] += 1
        except:
            dict[i.upper()] = 1

n = 0
for lettre in dict:
    if n == 0:
        max = dict[lettre]
        L = lettre
        n = 1
    if dict[lettre] > max :
        max = dict[lettre]
        L = lettre

print(L)









































