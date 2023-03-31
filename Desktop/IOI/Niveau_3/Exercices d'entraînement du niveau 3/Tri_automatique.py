## Method with complexity O(N1+N2) (we use property of dictionary in python)
N1 = int(input())
L1 = list(map(int, input().split()))

N2 = int(input())
L2 = list(map(int, input().split()))

dict = {}
for element in L1:
    dict[element] = 1
n = 0
for element in L2:
    if element in dict:
        n += 1
print(n)

## Method with complexity [N1*log(N1) + N2*log(N2) + N1*log(N2) < O(max(N1,N2)*log(max(N1,N2)))]
def Binary_search(element, List):
    start = 0
    end = len(List)-1
    mid = end // 2
    while start <= end:
        if element == List[mid]:
            return True
        elif List[mid] > element:
            end = mid - 1
        else:
            start = mid + 1
        mid = (start + end) // 2
    return False

N1 = int(input())
L1 = list(map(int, input().split()))

N2 = int(input())
L2 = list(map(int, input().split()))

L1.sort()
L2.sort()
n = 0
for element in L1:
    if Binary_search(element, L2):
        n += 1

print(n)



            