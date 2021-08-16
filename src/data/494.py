from collections import defaultdict

N, Q = map(int, input().split())
edges = defaultdict(list)
for _ in range(N - 1):
    a, b = map(int, input().split())
    edges[a].append(b)
    edges[b].append(a)
queries = []
for _ in range(Q):
    queries.append(list(map(int, input().split())))

binary_grouping = [None] * (N + 1)

# dfs
stack = [(1, 0)]

while stack:
    node, color = stack.pop()
    if binary_grouping[node] is not None:
        continue
    binary_grouping[node] = color
    for next_node in edges[node]:
        stack.append((next_node, 1 - color))

for c, d in queries:
    if binary_grouping[c] == binary_grouping[d]:
        print('Town')
    else:
        print('Road')
