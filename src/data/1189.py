import sys

sys.setrecursionlimit(500000)
N, Q = map(int, input().split())
A = [-1 for _ in range(N)]
T = [set() for _ in range(N)]
for _ in range(N - 1):
    a, b = map(int, input().split())
    T[a - 1].add(b - 1)
    T[b - 1].add(a - 1)
A[0] = 0


def dfs(i):
    for t in T[i]:
        if A[t] == -1:
            A[t] = (A[i] + 1) % 2
            dfs(t)


dfs(0)
for i in range(Q):
    x, y = map(int, input().split())
    if A[x - 1] == A[y - 1]:
        print("Town")
    else:
        print("Road")
