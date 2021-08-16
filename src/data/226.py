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
depth_lst = [-1 for _ in range(n)]
dq = deque()
dq.append((0, 0))
while (len(dq) > 0):
    node, depth = dq.popleft()
    depth_lst[node] = depth
    for child in node_lst[node]:
        if depth_lst[child] >= 0: continue
        dq.append((child, depth + 1))
        # print("depth_lst:",depth_lst)

for _ in range(q):
    ans = 0
    c, d = map(int, input().split())
    c -= 1
    d -= 1
    ans = depth_lst[c] + depth_lst[d]
    ans %= 2
    print(["Town", "Road"][ans])
