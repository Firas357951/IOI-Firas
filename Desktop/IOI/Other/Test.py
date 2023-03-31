#import sys
#node1, node2 = sys.stdin.readline().strip().split()
#print(node1)
#print(node2)
import time
start = time.time()
s = 0
for _ in range(10000000):
    s += 1


end = time.time()
print(end - start)
