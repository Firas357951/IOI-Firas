import sys

def Closest_Search(element, List):
    if element < List[0]:
        return List[0]
    if element > List[-1]:
        return List[-1]
    start = 0
    end = len(List) - 1
    mid = end // 2
    while start <= end:
        if List[mid] == element:
            return element
        elif List[mid] > element:
            end = mid - 1
        else:
            start = mid + 1
        mid = (start + end) // 2
    if abs(List[end+1] - element) < abs(List[end] - element):
        return List[end+1]
    else:
        return List[end]

N = int(input())
L = list(map(int, input().split()))
Q = int(input())

L.sort()
for _ in range(Q):
    x = int(sys.stdin.readline().strip())
    print(Closest_Search(x, L))
