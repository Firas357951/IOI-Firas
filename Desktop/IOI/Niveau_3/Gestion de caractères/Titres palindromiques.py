def Palindrome(ch):
    ch = ch.upper()
    ch = "".join(ch.split())
    for idx in range(len(ch)//2):
        if ch[idx] != ch[len(ch)-1-idx]:
            return False
    return True

N = int(input())


for _ in range(N):
    ch = str(input())
    if Palindrome(ch):
        print(ch)