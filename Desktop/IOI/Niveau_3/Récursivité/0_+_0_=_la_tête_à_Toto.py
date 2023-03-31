N = int(input())

def draw(N):
    if N == 0:
        return str(0)
    else:
        return '(' + draw(N-1) + ' + ' + draw(N-1) + ')'
    
print('0 = ' + draw(N))