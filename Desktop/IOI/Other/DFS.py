G = {
    'A':  ['B', 'C', 'D'],
    'B':  ['E', 'F', 'G'],
    'C':  [],
    'D':  ['H'],
    'E':  ['A'],
    'F':  [],
    'G':  [],
    'H':  []
}


pile = ['A']
Memo = {'A': None}
while pile != []:
    print(pile)
    N = pile[-1]
    if G[N] != []:
        element = G[N].pop(0)
        if not(element in Memo):
            Memo[element] = None
            pile.append(element)
    else:
        pile.pop(-1)
    









