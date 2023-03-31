## This solution do not theoretically differ from the next solution, they have the same complexity, but for certain tests this solution is better because
# it stops early when there are no enough rooms for the shows.
import sys
def main():
    inp = sys.stdin.readline
    S, R = map(int, inp().split())
    List = [None] * R
    for idx in range(R):
        a, b = inp().split()
        List[idx] = (int(a), int(b))
        
    Idx = sorted(range(R), key=lambda k: List[k])    
    Salle = [None] * S
    for index in Idx:
        element = List[index]
        a = element[0]
        added = False
        for idx, salle in enumerate(Salle):
            if salle == None:
                added = True
                Salle[idx] = element
                List[index] = idx
                break
            elif a >= salle[1]:
                added = True
                List[index] = idx
                Salle[idx] = element
                break
        if not(added):
            break
    if not(added):
        print('NON')
    else:
        print('OUI')
        print(' '.join([str(List[idx]+1) for idx in range(R)]))
main()
            
## Solution that validates 94% of tests
import sys
def main():
    inp = sys.stdin.readline
    S, R = map(int, inp().split())
    List = [None] * R
    for idx in range(R):
        a, b = inp().split()
        List[idx] = (int(a), int(b))
        
    Idx = sorted(range(R), key=lambda k: List[k])
    Memo = [False] * R
    i = 1
    n = 0
    while (i <= S) and (n < R):
        max = 0
        for idx in Idx:
            element = List[idx]
            if not(Memo[idx]):
                if (element[0] >= max):
                    max = element[1]
                    List[idx] = i
                    n += 1
                    Memo[idx] = True
        i += 1 

    if n == R:
        print('OUI')
        print(' '.join([str(List[idx]) for idx in range(R)]))
    else:
        print('NON')
main()
            
            
                
