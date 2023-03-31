import sys
def main():
   H, L, D = map(int, input().split())
   Matrix = [None] * H
   for idx in range(H):
       Line = list(map(int, sys.stdin.readline().strip().split()))
       Matrix[idx] = Line
   
   n = 1
   x = 0
   y = 0
   direction = [(1,0), (0,1), (-1,0), (0,-1)]
   if D == 0:
      print(0,0)
   while (x != H-1) or (y != L-1):
       for dir_x, dir_y in direction:
           if ((x + dir_x >= 0) and (x + dir_x < H)) and ((y + dir_y >= 0) and (y + dir_y < L)):
               if Matrix[x + dir_x][y + dir_y] == 0:
                   Matrix[x + dir_x][y + dir_y] = 1
                   x += dir_x
                   y += dir_y
                   n += 1
                   if n % (D+1) == 0:
                       print(x, y)
                   break
main()


## Only validates 80% of tests
import sys
def main():
    def ispoint(pos, H, L):
        x = pos[0]
        y = pos[1]
        if ((x >= 0) and (x < H)) and ((y >= 0) and (y < L)):
            return True
        return False

    def Next_pos(Prev_pos, pos, Matrix, H, L):
        List_x = [0, 1, -1, 0]
        List_y = [1, 0, 0, -1]
        for dir in range(4):
            x = pos[0] + List_x[dir]
            y = pos[1] + List_y[dir]
            if ispoint((x, y), H, L):
                if (Matrix[x][y] == 0) and (x, y) != Prev_pos:
                    return (x, y)
        
    H, L, D = map(int, input().split())
    Matrix = [None] * H
    for idx in range(H):
        Line = list(map(int, sys.stdin.readline().strip().split()))
        Matrix[idx] = Line
        
    dir_x = [0, 1]
    dir_y = [1, 0]
    for dir in range(2):
        x = dir_x[dir]
        y = dir_y[dir]
        if Matrix[x][y] == 0:
            pos = (x, y)
            break
        
    if D == 0:
        print(0, 0)
    Memo = []
    Prev_pos = (0, 0)
    n = 2
    while pos != None:
        if n % (D+1) == 0:
            Memo.append((pos[0], pos[1]))
        pos, Prev_pos = Next_pos(Prev_pos, pos, Matrix, H, L), pos
        n += 1
    for element in Memo:
        sys.stdout.write([element[0], element[1]])
main()