import sys

input = sys.stdin.readline
from collections import defaultdict, deque


def II():
    return int(input())


def IS():
    return input().rstrip()


def MI():
    return map(int, input().split())


def LI():
    return list(map(int, input().split()))


def MS():
    return input().rstrip().split()


def LS():
    return list(input().rstrip())


n, Q = MI()
d = defaultdict(list)
for i in range(n - 1):
    a, b = MI()
    a -= 1
    b -= 1
    d[a].append(b)
    d[b].append(a)


def biper(n: int, d: defaultdict(list)):
    seen = [0] * n
    parity = [0] * n
    q = deque()
    q.append((0, 0))
    while q:
        v, p = q.pop()
        if seen[v] == 0:
            seen[v] = 1
            parity[v] = p
        else:
            continue

        for to in d[v]:
            if seen[to] == 0:
                if p == 0:
                    q.appendleft((to, 1))
                else:
                    q.appendleft((to, 0))
            else:
                continue
    return parity


l = biper(n, d)
# print(l)

for i in range(Q):
    C, D = MI()
    C -= 1
    D -= 1
    if l[C] == l[D]:
        print('Town')
    else:
        print('Road')
