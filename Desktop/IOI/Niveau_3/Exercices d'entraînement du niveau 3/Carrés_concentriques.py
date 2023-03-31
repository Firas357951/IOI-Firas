N = int(input())
ch = input()

taille = 2*N-1
Matrix = [[''] * taille for _ in range(taille)]
for line in range(N):
    for col in range(line+1):
        Pos = [(line, col), (col, line), 
               (taille-1-line, col), (col, taille-1-line),
               (line, taille-1-col), (taille-1-col, line),
               (taille-1-col, taille-1-line), (taille-1-line, taille-1-col)
              ]
        letter = ch[len(ch)-1-col]
        for (i, j) in Pos:
            Matrix[i][j] = letter
        
for line in range(taille):
    print(''.join(Matrix[line]))
















