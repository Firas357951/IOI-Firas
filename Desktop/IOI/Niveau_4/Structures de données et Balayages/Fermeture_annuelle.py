import sys
def main():
    inp = sys.stdin.readline
    S, F = map(int, inp().split())
    List = []
    for _ in range(F):
        a, b = inp().split()
        if int(a) < int(b):
            List.append((int(a), int(b)))
        else:
            List.append((0, int(b)))
            List.append((int(a), S))
    List.sort()
    Max = 0
    i = 0
    for element in List:
        a, b = element
        if i < a:
            if (a - i) > Max:
                Max = (a - i)
            i = b
        elif i < b:
            i = b      
    print(max(Max, (S-i + List[0][0]))) 
main()