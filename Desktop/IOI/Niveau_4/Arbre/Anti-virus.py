def mask(code, element):
    element = str(element)
    if len(element) != len(code):
        return False
    else:
        for idx, letter in enumerate(code):
            if idx == 0 and letter == '?':
                if element[idx] == 0:
                    return False     
            elif letter == '?':
                pass
            elif letter != element[idx]:
                return False
    return True
            
def Children(Tree):
    Child = {}
    for idx, n in enumerate(Tree):
        try:
            Child[n].append(idx+1)
        except:
            Child[n] = []
            Child[n].append(idx+1)
    return Child
    

def Node_children(node, Tree):
    try:
        Children = Tree[node]
        return Children
    except:
        return []


def BFS(node, Tree):
    L = [node]
    Q = [node]
    while Q != []:
        N = Node_children(Q[0], Tree)
        Q.pop(0)
        Q.extend(N)
        L.extend(N)
    return L
             

N = int(input())
L = list(map(int, input().split(' ')))
code = str(input())

Tree = Children(L)

L = BFS(0, Tree)
L.pop(0)

for node in L:
    if mask(code, node):
        print(node, end= ' ')
        

















