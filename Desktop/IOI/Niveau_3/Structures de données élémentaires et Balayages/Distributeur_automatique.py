## Putting the code inside a main() function decreases execution time by 20%

import sys
def main():
    N = int(input())
    file = []
    for _ in range(N):
        q, date = map(int, sys.stdin.readline().split())
        if q > 0:
            for _ in range(q):
                file.append(date)
        else:
            for _ in range(-q):
                file.pop(0)

    print(min(file))
main()
