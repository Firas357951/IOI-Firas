def main():
    N, k = map(int, input().split())

    def Write(Course, act, k):
        if k == 0:
            print(' '.join([str(element) for element in Course]))
        elif (N-act) >= k:
            for number in range(act+1, N+1):
                Write(Course + [number], number, k-1)

    Write([], 0, k)
main()