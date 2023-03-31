from sys import stdin

Test = {
    'Firas' : True,
    '()' : True,
    '(' : False,
    ')(' : False,
    '(())' : True,
    '((((()))))' : True,
    '(ok)' : True,
    '())(' : False,    
    '(()(()))()((((()))))': True
       }

def Testing(func):
    print('Testing...')
    for key in Test:
        result = func(key)
        B = (result == Test[key])
        if not(B):
            print(key)
            return B
    return True

def BP_0(ch):
    Stack = []
    for letter in ch:
        if letter == '(':
            Stack.append(letter)
        elif letter == ')':
            if len(Stack) == 0:
                return False
            else:
                Stack.pop(-1)
    return len(Stack) == 0

def BP_1(ch):
    n = 0
    idx = 0
    while (idx < len(ch)) and (n >= 0):
        letter = ch[idx]
        if letter == '(':
            n += 1
        elif letter == ')':
            n -= 1
        idx += 1
    return n == 0
    
def BP_2(ch, n = 0):
    if n < 0:
        return False
    elif ch == '':
        return n == 0
    else:
        letter = ch[0]
        if letter == '(':
            return BP_2(ch[1:], n + 1)
        elif letter == ')':
            return BP_2(ch[1:], n - 1)
        else:
            return BP_2(ch[1:], n)

def BP_3(ch):
    
    while len(ch) != 0: 
        idx_end = ch.find(')')
        if idx_end == -1:
            return ch.find('(') == -1
        else:
            idx_start = ch[:idx_end].rfind('(') 
            if idx_start == -1:
                return False
            else:
                ch = ch[:idx_start] + ch[idx_end + 1:]
    return True

def BP_4(ch):
    
    idx_end = ch.find(')')
    if idx_end == -1:
        return ch.find('(') == -1
    else:
        idx_start = ch[:idx_end].rfind('(') 
        if idx_start == -1:
            return False
        else:
            return BP_4(ch[:idx_start] + ch[idx_end + 1:])

def BP_5(ch):
    if ch == '':
        return True
    else:
        letter = ch[0]
        if letter == ')':
            return False
        elif letter == '(':
            idx = ch.find(')')
            if idx == -1:
                return False
            else:
                return BP_5(ch[1:idx]) and BP_5(ch[idx+1:])
        else:
            return BP_5(ch[1:])


Testing(BP_5)




