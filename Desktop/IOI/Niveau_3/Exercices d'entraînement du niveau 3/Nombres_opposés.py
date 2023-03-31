def binary_search(element, List):
    start = 0
    end = len(List)-1
    mid = end // 2
    while start <= end:
        if element == List[mid]:
            return True
        elif element > List[mid]:
            start = mid + 1
        else:
            end = mid - 1
        mid = (start + end) // 2
    return False

N = int(input())
L = list(map(int, input().split()))
Memo = []
L1 = []
L2 = []
for element in L:
    if element > 0 :
        L1.append(element)
    else:
        L2.append(-element)
L1.sort()
L2.sort()
n = 0
for idx, element in enumerate(L1):
    if binary_search(element, L2) and not(binary_search(element, Memo)): 
        n += 1
        Memo.append(element)
print(n)











