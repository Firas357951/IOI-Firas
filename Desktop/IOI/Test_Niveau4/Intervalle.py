def ExtractM(I):
        A = []
        n = 0
        for item in I:
            A.append(n - item[2])
            
            n +=1
        print(A)
        return max(A)
    
def Ajout(I):
    A = [(I[0][0], I[0][1], 0)]
    i = 1
    while i <= len(I)-1:
        if I[i] == I[i-1]:
            k = A[i-1][2]
            A.append((I[i][0], I[i][1], k))
        else:
            A.append((I[i][0], I[i][1], i))
        i += 1   
    return A



N = int(input())
I = []
for i in range(N):
    a,b = input().split(' ')
    I.append((int(a),int(b)))
    
I = sorted(I, key=lambda tup:(tup[0], -tup[1]))
print(I)
I = Ajout(I)
print(I)
I = sorted(I, key=lambda tup:(tup[1], -tup[0]))
print(I)
print(ExtractM(I))




