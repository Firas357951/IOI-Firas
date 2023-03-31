def find_line(N, symbol, Matrix):
    if N < 5:
        return False
    else:
        for line in range(N):
            for start in range(N-4):
                if Matrix[line][start: start+5] == [symbol] * 5:
                    return True
        for col in range(N):
            for start in range(N-4):
                L = []
                for idx in range(5):
                    L.append(Matrix[start + idx][col])
                if L == [symbol] * 5:
                    return True
        for i in range(N-4):
            line, col = 0, i
            L = []
            for idx in range(5):
                L.append(Matrix[line+idx][col+idx])
            if L == [symbol] * 5:
                return True
            line, col = i, 0
            L = []
            for idx in range(5):
                L.append(Matrix[line+idx][col+idx])
            if L == [symbol] * 5:
                return True
        for i in range(N-4):
            line, col = 0, N-1-i
            L = []
            for idx in range(5):
                L.append(Matrix[line+idx][col-idx])
            if L == [symbol] * 5:
                return True
            line, col = i, N-1
            L = []
            for idx in range(5):
                L.append(Matrix[line+idx][col-idx])
            if L == [symbol] * 5:
                return True
    return False


N = int(input())
Matrix = []
for line in range(N):
    line = list(map(int, input().split()))
    Matrix.append(line)

B1 = find_line(N, 1, Matrix)
B2 = find_line(N, 2, Matrix)
if B1:
    print(1)
elif B2:
    print(2)
else:
    print(0)
         
        
        
        
        
        
        
        