import sys

sys.setrecursionlimit(10**8)

n, q = [int(i) for i in input().split()]
tree = [[] for i in range(n)]
for i in range(n - 1):
    a, b = [int(i) for i in input().split()]
    tree[a - 1].append(b - 1)
    tree[b - 1].append(a - 1)
cd = [[int(i) - 1 for i in input().split()] for j in range(q)]

depth = [-1] * n


def dp(node: int, pare: int):
    depth[node] = depth[pare] + 1
    for child in tree[node]:
        if child == pare:
            continue
        dp(child, node)


dp(0, -1)

for qu in cd:
    if (depth[qu[0]] + depth[qu[1]]) % 2 == 0:
        print('Town')
    else:
        print('Road')
