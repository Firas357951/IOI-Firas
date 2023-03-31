def BFS(Node, AdjList):
    n = 1
    file = [Node]
    visited = {}
    for i in range(len(AdjList)):
        visited[i] = False
    visited[Node] = True
    while file != []:
        for element in AdjList[file[0]]:
            if not(visited[element]):
                file.append(element)
                visited[element] = True
                n += 1
        print(file)
        file.pop(0)
    return n
dict = {1: [8], 8: [1, 3], 3: [4, 8, 2], 4: [3], 2: [3, 6], 6: [2, 7, 5, 0], 7: [6], 5: [6, 9], 9: [5], 0: [6]}
print(BFS(1, dict))

















