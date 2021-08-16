from collections import deque

n, q = map(int, input().split())
node_lst = [[] for _ in range(n)]
for _ in range(n - 1):
    a, b = map(int, input().split())
    a -= 1
    b -= 1
    node_lst[a].append(b)
    node_lst[b].append(a)
# print(node_lst)
dep_lst = [-1 for _ in range(n)]
que = deque()
que.append((0, 0))

while len(que) > 0:
    node, depth = que.popleft()
    dep_lst[node] = depth
    # print(node_lst[node])
    for child in node_lst[node]:
        if dep_lst[child] >= 0: continue
        que.append((child, depth + 1))

for _ in range(q):
    ans = 0
    fr, to = map(int, input().split())
    fr -= 1
    to -= 1
    ans = (dep_lst[fr] + dep_lst[to]) % 2
    print(["Town", "Road"][ans])
