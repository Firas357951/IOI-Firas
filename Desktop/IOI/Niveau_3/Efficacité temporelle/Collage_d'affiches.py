import sys
N = int(input())

pile = []
for _ in range(N):
    List = sys.stdin.readline().strip().split(' ')
    if len(List) > 1:    
        i = int(List[1])
        if len(pile) == 0:
            pass
        else:
            while pile[-1] <= i:
                pile.pop(-1)
                if len(pile) == 0:
                    break 
        pile.append(i)        
    else:
        print(len(pile))