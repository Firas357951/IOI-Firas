import sys
def main():
    L, N = map(int, input().split())
    if L == 0:
        return 0
    List = list(map(int, sys.stdin.readline().split()))
    List.sort()
    Diff = [j-i for i, j in zip(List, List[1:])]
    max = 0
    i, j, s = (0, 0, 0)
    while j < N-1:
        while (s + Diff[j]) <= L:
            s += Diff[j]
            j += 1
            if j == N-1:
                break
        if (j - i) > max:
            max = j - i
        if j == N-1:
                break
        while (s + Diff[j]) > L:
            s -= Diff[i] 
            i += 1
    return(max + 1)

print(main())  


    