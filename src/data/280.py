n, q = map(int, input().split())
edge = [[] for i in range(n)]
for i in range(n - 1):
    a, b = map(int, input().split())
    a -= 1
    b -= 1
    edge[a].append(b)
    edge[b].append(a)
# print("edge:",edge)
from collections import deque

que = deque()
depth = [-1 for i in range(n)]
# depth[0]=0
que.append((0, 0))
# print("que:",que,"depth:",depth)
while len(que) > 0:

    node, dep = que.popleft()
    depth[node] = dep
    # print("q:",q)
    # tmp=0
    # print("Q:",q)
    # t=edge(q)
    # print(t)
    # tmp=0
    for child in edge[node]:
        if depth[child] < 0:
            que.append((child, dep + 1))
        else:
            continue

for j in range(q):
    ans = 0
    a, b = map(int, input().split())
    a -= 1
    b -= 1
    ans += depth[a] + depth[b]
    ans %= 2
    print(["Town", "Road"][ans])
