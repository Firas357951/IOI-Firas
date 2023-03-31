ch = str(input())

def f(ch):
    if len(ch) == 1:
        print(ch, end='')
    else:
        f(ch[1:])
        print(ch[0], end='')
f(ch)