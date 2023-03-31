import sys

def binary_search(element, List):
    start = 0
    end = len(List) - 1
    mid = end // 2
    while start <= end:
        if List[mid] == element:
            return True
        elif element > List[mid]:
            start = mid + 1
        else:
            end = mid - 1
        mid = (start + end) // 2 
    return False

N = int(input())
L = list(map(int, input().split()))
Q = int(input())

L.sort()
for _ in range(Q):
    x = int(sys.stdin.readline().strip())
    if binary_search(x, L):
        print(1)
    else:
        print(0)

