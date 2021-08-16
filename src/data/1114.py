import bisect, collections, copy, heapq, itertools, math, sys

sys.setrecursionlimit(10**7)


def I():
    return int(sys.stdin.readline().rstrip())


def LI():
    return list(map(int, sys.stdin.readline().rstrip().split()))


def S():
    return sys.stdin.readline().rstrip()


def LS():
    return list(sys.stdin.readline().rstrip().split())


n, q = LI()
ab = [LI() for i in range(n - 1)]

cd = [LI() for i in range(q)]

length = [-1 for i in range(n)]
path = [[] for i in range(n)]
for i in range(n - 1):
    a, b = ab[i][0] - 1, ab[i][1] - 1
    path[a].append(b)
    path[b].append(a)

que = collections.deque()
que.append((0, 0))

while len(que) > 0:
    now, step = que.popleft()
    length[now] = step
    for i in path[now]:
        if length[i] != -1: continue
        que.append((i, step + 1))

for i in range(q):
    c, d = cd[i][0] - 1, cd[i][1] - 1

    if (length[c] + length[d]) % 2 == 0:
        print("Town")
    else:
        print("Road")
