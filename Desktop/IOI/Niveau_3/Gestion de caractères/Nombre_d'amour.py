def Nombre_Amour(ch):
    s = 0
    for letter in ch:
        s += ord(letter) - ord("A")
    while s >= 10:
        s = sum([int(i) for i in str(s)])
    return s
    
ch = str(input())

for prenom in ch.split():
    print(Nombre_Amour(prenom), end= ' ')
    
