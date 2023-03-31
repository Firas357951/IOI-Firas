def count(x0, y0, Matrix, H, L):
    if (x0 > 0 and x0 < H-1) and (y0 > 0 and y0 < L -1):
        dir_x = [1, 0, 0, -1]
        dir_y = [0, 1, -1, 0]
        count = 0
        for direction in range(4):
            x = x0 + dir_x[direction]
            y = y0 + dir_y[direction]
            if Matrix[x][y] == "#":
                count += 1
        if count == 4:
            return True
    return False

def erosion(H, L, Matrix):
    M = [['.']* L for _ in range(H)]
    for line in range(H):
        for col in range(L):
            if Matrix[line][col] == '#':
                if count(line, col, Matrix, H, L):
                    M[line][col] = '#'
    return M

N = int(input())
H, L = map(int, input().split())
Matrix = []
for _ in range(H):
    line = list(str(input()))
    Matrix.append(line)
    
for _ in range(N):
    Matrix = erosion(H, L, Matrix)

for line in range(H):
    for col in range(L):
        print(Matrix[line][col], end='')
    print()
    