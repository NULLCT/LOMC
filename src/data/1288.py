#!/usr/bin/env python3
import sys

input = sys.stdin.readline

n, q = map(int, input().split())
edge = [[] for _ in range(n)]
for _ in range(n - 1):
    a, b = map(int, input().split())
    a -= 1
    b -= 1
    edge[a].append(b)
    edge[b].append(a)


def dfs(p, v):
    st = [(p, v, 0)]
    visited = [-1] * n
    while st:
        p, v, oe = st.pop()
        visited[v] = oe
        oe = 1 - oe
        for nv in edge[v]:
            if nv == p:
                continue
            st.append((v, nv, oe))
    return visited


visited = dfs(-1, 0)
# print(visited)

for _ in range(q):
    c, d = map(int, input().split())
    c -= 1
    d -= 1
    if visited[c] == visited[d]:
        print("Town")
    else:
        print("Road")
