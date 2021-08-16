import collections


def bfs(tree):
    d = collections.deque([])
    d.append(1)
    level = {1: 0}
    vis = collections.defaultdict(bool)
    vis[1] = True
    while d:
        u = d.popleft()
        for v in tree[u]:
            if not vis[v]:
                vis[v] = True
                level[v] = level[u] + 1
                d.append(v)
    return level


n, q = map(int, input().split())
tree = collections.defaultdict(list)
for i in range(n - 1):
    a, b = map(int, input().split())
    tree[a].append(b)
    tree[b].append(a)
level = bfs(tree)
for k in range(q):
    a, b = map(int, input().split())
    if (level[a] + level[b]) % 2 == 0:
        print("Town")
    else:
        print('Road')
