def search(element, list):
   for idx, e in enumerate(list):
      if e == element:
         return idx

N = int(input())
L = list(map(int, input().split()))
H = []
n = 0
for auto in range(1, N+1):
   idx = search(auto, L)
   while idx>0:
      if L[idx-1] > L[idx]:
         H.append((L[idx-1], L[idx]))
         L[idx-1], L[idx] = L[idx], L[idx-1]
         idx -= 1
         n += 1
      else:
         break

print(n)
for element in H:
   print(element[0], element[1])


