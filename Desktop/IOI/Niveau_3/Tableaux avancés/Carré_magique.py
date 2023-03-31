def C1(N, Matrix):
    List = [True] * (N*N)
    for Lig in range(N):
        for Col in range(N):
            number = Matrix[Lig][Col] 
            if number > N**2 or number <= 0:
                return False
            elif List[number-1]:
                List[number-1] = False
            else:
                return False
    return True

def C2(N, Matrix):
    s0 = sum(Matrix[0])
    for i in range(1, N):
        if sum(Matrix[i]) != s0:
            return (None, False)
    return (s0, True)

def C3(N, Matrix):
    s0 = 0
    for i in range(N):
            s0 += Matrix[i][0]
    for j in range(1, N):
        s = 0
        for i in range(N):
            s += Matrix[i][j]
        if s != s0:
            return (None, False)
    return (s0, True)

def C4(N, Matrix):
    s0 = 0
    for i in range(N):
        s0 += Matrix[i][i]
    s = 0
    for i in range(N):
        s += Matrix[i][N-1-i]
    if s == s0:
        return (s0, True)
    else:
        return (None, False)
    
N = int(input())    
L = []
for _ in range(N):
    Ligne = list(map(int, input().split()))
    L.append(Ligne)
     
if C1(N, L):
    s2, B2 = C2(N, L)
    s3, B3, = C3(N, L)
    s4, B4 = C4(N, L)
    if B2 and B3 and B4:
        if s2 == s3 and s4 == s2:
            print("yes")
        else:
            print('no')
    else:
        print('no')    
else:
    print('no')

