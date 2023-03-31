def HexaToInt(ch):
    ch = '0x' + ch 
    return int(ch, 0)
def hexa(n):
    return hex(n)[2:]

N = HexaToInt(input())

M = 0
for _ in range(N):
    M += HexaToInt(input())

Moy = int(M / N)
print(hexa(Moy).upper())
