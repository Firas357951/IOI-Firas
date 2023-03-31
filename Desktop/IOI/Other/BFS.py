Tree = [3, 3, 7, 3, 6, 7, 0, 0]

def Children(Tree):
    Child = {}
    for idx, n in enumerate(Tree):
        try:
            Child[n].append(idx+1)
        except:
            Child[n] = []
            Child[n].append(idx+1)
    return Child


Tree = Children(Tree)
    

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

print(BFS(0, Tree))
















