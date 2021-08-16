from collections import deque


def dfs1():  # depthの決定
    stack = deque()
    stack.append((0, 0))  # (index, depth)
    while stack:
        cur, dep = stack.pop()
        for post in graph[cur]:
            if depth[post] == -1:
                stack.append((post, dep + 1))
                depth[post] = dep + 1


n, q = map(int, input().split())
graph = [[] for _ in range(n)]
for _ in range(n - 1):
    a, b = map(int, input().split())
    graph[a - 1].append(b - 1)
    graph[b - 1].append(a - 1)

depth = [-1] * n
depth[0] = 0

dfs1()

CD = [list(map(int, input().split())) for _ in range(q)]

for c, d in CD:
    c -= 1
    d -= 1
    if (depth[c] - depth[d]) % 2 == 0:
        print("Town")
    else:
        print("Road")
