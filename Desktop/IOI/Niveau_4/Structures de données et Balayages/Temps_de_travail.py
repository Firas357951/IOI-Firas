import sys
def main():
    N = int(input())
    Intervals = [None] * N
    inp = sys.stdin.readline
    for idx in range(N):
        a, b = inp().split()
        Intervals[idx] = (int(a), int(b))

    Intervals.sort()

    s = 0
    I = (0, 0)
    for interval in Intervals:
        a, b = interval
        if I[1] < a:
            s += (b-a)
            I = (a, b)
        elif I[1] < b:
            s += (b - I[1])
            I = (I[0], b)

    print(s)         
main()
















