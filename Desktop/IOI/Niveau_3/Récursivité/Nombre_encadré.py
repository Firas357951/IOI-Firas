N, Bct_num = map(int, input().split())

def f(N, Bct_num):
    if Bct_num == 0:
        return str(N)
    else:
        return '['+ f(N, Bct_num - 1) +']' 

print(f(N, Bct_num))