from collections import deque


def BFS(start, tree):
    search = deque()
    search.append(start)
    visited = {start[0]}  # リストでやるとおそい
    #kyori = {}
    while len(search) > 0:
        # print(search)
        node, depth = search.popleft()
        depth_list[node] = depth
        # print(node,depth)
        # if node in visited:
        #  continue
        for i in tree[node]:
            if i not in visited:
                search.append([i, depth + 1])
                visited.add(i)


n, q = map(int, input().split())

edges = [list() for i in range(n)]
for i in range(n - 1):
    a, b = map(int, input().split())
    a, b = a - 1, b - 1
    edges[a].append(b)
    edges[b].append(a)
depth_list = [0] * n
BFS((0, 0), edges)
#print(depth_list)

for k in range(q):
    c, d = map(int, input().split())
    c, d = c - 1, d - 1
    if (depth_list[c] - depth_list[d]) % 2 == 0:
        print("Town")
    else:
        print("Road")
