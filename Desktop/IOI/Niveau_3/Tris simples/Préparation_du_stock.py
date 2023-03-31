n, m = map(int, input().split())
L = list(map(int, input().split()))

Insert = list(map(int, input().split()))
def binary_search(element, List):
    start = 0
    end = len(List)-1
    while start <= end:
        mid = (start + end)//2
        a = List[mid]
        if element <= a:
            end = mid - 1
        else:
            start = mid + 1
    return end + 1
    
for element in Insert:
   idx = binary_search(element, L)
   print(idx, end=' ')
   L.insert(idx, element)
print()
for element in L:
   print(element, end= ' ')
























