N = int(input())
I = input().split(' ')
n = int(input())
J = input().split(' ')
    
for i in range(n):
    a = J[i]
    ch = ''
    while a != '0':
        ch = str(a) + ' ' + ch
        a = I[(int(a) - 1)]
    print(ch)