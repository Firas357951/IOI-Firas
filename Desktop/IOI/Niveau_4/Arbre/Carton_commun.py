def Father(item, List):
    return List[item - 1]

def Branch(item, List):
    a = item
    L = [a]
    while a != 0:
        a = Father(a, List)
        L.append(a)
    return L


def CommonFather(n, m, List):
    L = Branch(n, List)

    while not(m in L) :
        m = Father(m, List)
        
    return m

n = int(input())

I = input().split(' ')
I = [int(i) for i in I]

N = int(input())

for i in range(N):
    n , m = [int(j) for j in input().split(" ")]
    print(CommonFather(n, m, I))























































