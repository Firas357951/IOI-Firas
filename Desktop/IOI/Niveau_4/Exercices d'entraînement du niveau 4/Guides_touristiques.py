from sys import stdin
def main():
    inp = stdin.readline
    G, N = map(int, inp().split())
    List = [None] * N
    for idx in range(N):
        a, b = inp().split()
        List[idx] = (int(a), int(b))
        
    List.sort()
    Guide = [0] * G
    for element in List:
        available = False
        a, b = element
        for idx, g in enumerate(Guide):
            if g <= a:
                available = True
                Guide[idx] = b
                break
        if not(available):
            return 0
    return 1
print(main())