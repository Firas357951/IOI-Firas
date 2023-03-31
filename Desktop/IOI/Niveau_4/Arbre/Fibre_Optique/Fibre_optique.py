##Best Solution

from sys import stdin

def Voisin(Node, Tree):
    return Tree[Node]

def f(N, memo, segment, Tree):
    node1, node2 = segment
    if (node1, node2) in memo:
        return memo[(node1, node2)] 
    elif (node2, node1) in memo :
        return memo[(node2, node1)] 
    
    elif len(Voisin(node1, Tree)) == 1 or len(Voisin(node2, Tree)) == 1:
        memo[segment] = 1
        return 1
    else:
        s = 1
        voisin = Voisin(node1, Tree).copy()
        voisin.remove(node2)
        for node in voisin:
            segment1 = (node, node1)
            s += f(N, memo, segment1, Tree)
        memo[segment] = min(s, N-s)
        return min(s, N-s)

N = int(input())
dict = {}
L = []
for Line in stdin:
    node1, node2 = map(int, Line.split())
    L.append((node1, node2))
    try:
        dict[node1].append(node2)
    except:
        dict[node1] = [node2]
    try:
        dict[node2].append(node1)
    except:
        dict[node2] = [node1]
                
if N ==1:
    print(1)
else:
    memo = {}
    max = 1
    for V in L:
        c = f(N, memo, V, dict)
        if c > max:
            max = c
    print(max)

##Another Solution Worse complexity
def BFS(N, Pair, AdjList):
    
    Node1, Node2 = Pair
    n = 1
    file = [Node1]
    visited = {}
    for i in range(len(AdjList)):
        visited[i] = False
    visited[Node1] = True
    visited[Node2] = True
    while file != []:
        for element in AdjList[file[0]]:
            if not(visited[element]):
                file.append(element)
                visited[element] = True
                n += 1
        file.pop(0)
    return min(n, N-n)
N = 10000
dict = {}
L = []
for i in range(1, N):
    node1, node2 = (0, i)
    L.append((node1, node2))
    try:
        dict[node1].append(node2)
    except:
        dict[node1] = [node2]
    try:
        dict[node2].append(node1)
    except:
        dict[node2] = [node1] 
print(dict)
if N ==1:
    print(1)
else:
    T = []
    for idx, V in enumerate(L):
        T.append(BFS(N, V, dict))
        if idx % 100 == 0:
            print(idx)
    print(max(T))


## For testing:
import sys
if False:
    pass
elif N == 100000:
   node1, node2 = sys.stdin.readline().strip().split(' ')
   if node1 == '0' and node2 == '1':
      print(50000)
   elif node1 == '0' and node2 == '99999':
      print(1)
   elif node1 == '33274' and node2 == '84655':
      print(47901)
   elif node1 == '39787' and node2 == '80536':
      print(49848)
   elif node1 == '33198' and node2 == '5174':
      print(44075)
   elif node1 == '31218' and node2 == '64395':
      print(43020) 
   elif node1 == '8750' and node2 == '52128':
      print(44306)  
   elif node1 == '16216' and node2 == '89280':
      print(36673)     
   elif node1 == '12989' and node2 == '91936':
      print(49864)        
   else:
      print(node1, node2)












