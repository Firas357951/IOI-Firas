def inside(x, y):
    if x in range(8) and y in range(8):
        return True
    return False

def Cavalier(x0, y0):
    L = []
    List1 = [-2, 2]
    List2 = [-1, 1]
    for step_x in List1:
        for step_y in List2:
            x = x0 + step_x
            y = y0 + step_y
            if inside(x, y):
                L.append((x, y))
    for step_y in List1:
        for step_x in List2:
            x = x0 + step_x
            y = y0 + step_y
            if inside(x, y):
                L.append((x, y))
    return L

Matrix = []
for _ in range(8):
    Line = list(str(input()))
    Matrix.append(Line)

B = False
for line in range(8):
    for col in range(8):
        if Matrix[line][col] == 'C':
            L = Cavalier(line, col)
            for possibility in L:
                x, y = possibility
                if Matrix[x][y].islower():
                    print('yes')
                    B = True
                    break
        if B:
            break
    if B:
        break
if not(B):
    print('no')
        
            