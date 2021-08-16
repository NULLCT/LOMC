import sys

input = sys.stdin.readline
from collections import deque


def read():
    N, Q = map(int, input().strip().split())
    G = [list() for i in range(N)]
    for i in range(N - 1):
        a, b = map(int, input().strip().split())
        G[a - 1].append(b - 1)
        G[b - 1].append(a - 1)
    CD = []
    for i in range(Q):
        c, d = map(int, input().strip().split())
        CD.append((c - 1, d - 1))
    return N, G, CD


def solve(N, G, CD):
    depth = [-1 for i in range(N)]
    q = deque()
    depth[0] = 0
    q.append(0)
    while q:
        u = q.popleft()
        for v in G[u]:
            if depth[v] == -1:
                depth[v] = depth[u] + 1
                q.append(v)
    for c, d in CD:
        if (depth[c] + depth[d]) % 2 == 0:
            print("Town")
        else:
            print("Road")


if __name__ == '__main__':
    inputs = read()
    outputs = solve(*inputs)
    if outputs is not None:
        print("%s" % str(outputs))
