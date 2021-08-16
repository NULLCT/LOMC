n, q = map(int, input().split())
node_lst = [[] for _ in range(n)]
for _ in range(n - 1):
    a, b = map(int, input().split())
    a -= 1
    b -= 1
    node_lst[a].append(b)
    node_lst[b].append(a)
# print(node_lst)
from collections import deque

dq = deque()
dq.append((0, 0))
depth_lst = [-1 for _ in range(n)]
while (len(dq) > 0):
    node, depth = dq.popleft()
    depth_lst[node] = depth
    for child in node_lst[node]:
        if depth_lst[child] >= 0: continue
        dq.append((child, depth + 1))
# print(depth_lst)
for j in range(q):
    ans = 0
    fr, to = map(int, input().split())
    fr -= 1
    to -= 1
    ans = depth_lst[fr] + depth_lst[to]
    ans %= 2
    print(["Town", "Road"][ans])

# for i in range(q):
#     fr,to=map(int,input().split())
