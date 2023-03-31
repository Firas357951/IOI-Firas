## Method using set structure in Python
import sys
inp = sys.stdin.readline
def main():
    id = input()
    N = int(input())
    Relations =[inp().strip().split() for _ in range(N)]
    Friends = set()
    for relation in Relations:
        if id in relation:
            Friends.update(relation)
    Friends_of_Friends = set()
    for relation in Relations:
        id1, id2 = relation
        if id1 in Friends or id2 in Friends:
            Friends_of_Friends.update(relation)
    result = len(Friends_of_Friends - Friends - {id})
    print(result)
main()

## Method with little improvements validates 100% of tests
import sys
inp = sys.stdin.readline
def main():
    id = input()
    N = int(input())
    dict = {}
    Memo = [False] * 65001
    for _ in range(N):
        id1, id2 = inp().strip().split()
        try:
            dict[id1].append(id2)
        except:
            dict[id1] = [id2]
        try:
            dict[id2].append(id1)
        except:
            dict[id2] = [id1]
    Friends = dict[id]
    Memo[int(id)] = True
    n = 0
    for user in Friends:
        Memo[int(user)] = True
    for user in Friends:
        user_friend = dict[user]
        for friend in user_friend:
            if not(Memo[int(friend)]):
                Memo[int(friend)] = True
                n += 1
    print(n)
main()
## Method validates 90% of tests
import sys
def main():
    id = int(input())
    N = int(input())
    Graph = [[] for _ in range(65001)]
    Memo = [False] * 65001
    for _ in range(N):
        id1, id2 = map(int, sys.stdin.readline().strip().split())
        Graph[id1].append(id2)
        Graph[id2].append(id1)
    Friends = Graph[id]
    Memo[id] = True
    n = 0
    for user in Friends:
        Memo[user] = True
    for user in Friends:
        for friend in Graph[user]:
            if not(Memo[friend]):
                Memo[friend] = True
                n += 1
    print(n)
main()