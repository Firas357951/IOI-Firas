import sys
def main():
    inp = sys.stdin.readline
    def inter(a1, b1, a2, b2):
        List = [(a1, b1), (a2, b2)]
        List.sort()
        (a1, b1), (a2, b2) = List
        if a2 < b1:
            if b2 < b1:
                return b2-a2
            else:
                return b1-a2
        return 0

    a, b, c, d = map(int, input().split())
    N = int(input())
    Area = (c-a) * (d-b)
    for _ in range(N):
        x1, y1, x2, y2 = map(int, inp().split())
        Area -= inter(a, c, x1, x2) * inter(b, d, y1, y2)

    print(Area)
main()