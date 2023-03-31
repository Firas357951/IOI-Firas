def is_Varibale(Var):
    v = Var[0]
    if v != '_' and not(v.isalpha()):
        return False
    else:
        for idx in range(1, len(Var)):
            v = Var[idx]
            if v != '_' and not(v.isalpha()) and not(v.isdigit()):
                return False
    return True

N = int(input())

for _ in range(N):
    ch = str(input())
    if is_Varibale(ch):
        print("YES")
    else:
        print("NO")