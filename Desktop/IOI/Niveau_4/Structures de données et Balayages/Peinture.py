import sys

NbP, N = map(int, input().split())
L = list(map(int, sys.stdin.readline().strip().split()))

def Binary_search(element, List):
    start = 0
    end = len(List) - 1
    mid = end // 2
    while start <= end : 
        if List[mid] == element:
            return True
        elif element < List[mid]:
            end = mid - 1
        else:
            start = mid + 1
        mid = (start + end) // 2
    return False

B = True
for element in L:
    e = N - element
    if element > N:
        break
    if Binary_search(e, L):
        print("OUI")
        B = False
        break
if B:        
   print("NON")