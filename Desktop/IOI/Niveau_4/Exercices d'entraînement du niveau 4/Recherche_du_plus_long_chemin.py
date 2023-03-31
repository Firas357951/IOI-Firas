#L, C = map(int, input().split())
L, C = 10, 10
def Valid_point(x, y):
    if (x >= 0 and x < L) and (y >= 0 and y < C):
        return True
    return False

direction = {
    (1, 0) :  'S',
    (0, 1) :  'E',
    (-1, 0):  'N',
    (0, -1):  'O'
}
def dir(path):
    List = []
    for pos, next_pos in zip(path, path[1:]):
        List.append(direction[(next_pos[0]-pos[0], next_pos[1]-pos[1])])
    return List

#Matrix = []     
#for _ in range(L):
#    Matrix.append(list(input()))

M = [
     '##########',
     '.........#',
     '##...#.#.#',
     '#.###...##',
     '#.#...#..#',
     '#...####.#',
     '#.#.....##',
     '#..#..#..#',
     '#...#..#.#',
     '########.#'
    ]
Matrix = []     
for idx in range(L):
    Matrix.append(list(M[idx]))


Adj = {}
for line in range(L):
    for col in range(C):
        if Matrix[line][col] != '#':
            L_x = [-1, 1, 0, 0]
            L_y = [0, 0, -1, 1]  
            List = []
            for (dx, dy) in zip(L_x, L_y):
                x = line + dx
                y = col + dy
                if Valid_point(x, y) and Matrix[x][y] == '.':
                    List.append((x, y))
            Adj[(line, col)] = List    

max = ''
pile = [(1, 0)]
Memo = {(1, 0) : None}
while pile != []:
    N = pile[-1]
    if N == (L-1, C-2):
            path = dir(pile)
            if len(path) > len(max):
                max = path
            elif (len(path) == len(max)) and (path < max):
                max = path
    if Adj[N] != []:
        element = Adj[N].pop(0)
        if not(element in Memo):
            Memo[element] = None
            pile.append(element)
    else:
        pile.pop(-1)

print(len(path))
print(''.join(path))   
    

