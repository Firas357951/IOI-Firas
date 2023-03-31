import sys
inp = sys.stdin.readline
def main():
    L, _ = map(int, input().split())
    n = 0
    for _ in range(L):
        n += sum([1 for element in inp() if element =='#'])    
    print(n)
main()    
