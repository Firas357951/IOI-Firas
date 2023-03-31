## Optimized method
def main():
   ch = input()
   
   n = len(ch)
   Max = 1
   for idx in range(n):
       ix = 1
       for i in range(1, min(idx, n-1-idx)+1):
           if ch[idx + i] != ch[idx - i]:
               break
           ix += 1
       l1 = 2*ix-1
       if l1 > Max:
           Max = l1
           
   for idx in range(n-1):
       if ch[idx] == ch[idx+1]:
           jx = 1
           for j in range(1, min(idx, n-2-idx)+1):
               if ch[idx + j + 1] != ch[idx - j]:
                   break
               jx += 1
           l2 = 2*jx
           if l2 > Max:
               Max = l2
   
   print(Max)
main()

## Naive method
def Palindrome(ch):
    n = len(ch)
    for idx in range(n//2):
        if ch[idx] != ch[n - 1 - idx]:
            return False
    return True

ch = input()
n = len(ch)
max = n
B = False
for idx in range(n, 0, -1):
    for start in range(n-idx+1):
        word = ch[start: start+idx]
        if Palindrome(word):
            B = True
            max = idx
            break
    if B:
        break
print(max)