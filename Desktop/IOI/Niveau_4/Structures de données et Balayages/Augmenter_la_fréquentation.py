import sys
def main():
    N = int(input())
    List = [None] * N
    inp = sys.stdin.readline
    for idx in range(N):
        a, b = inp().split()
        List[idx] = (int(a), int(b))

    List.sort()

    max = 0
    Avg = 0
    for idx, element in enumerate(List):
        Avg = (Avg * (idx) + element[1])/(idx+1)
        if Avg >= max:
            max = Avg
            i = idx
    print(List[i][0])

main()