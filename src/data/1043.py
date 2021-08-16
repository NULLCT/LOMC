N, Q = map(int, input().split())

tree = [[] for _ in range(N + 1)]
for _ in range(N - 1):
    a, b = map(int, input().split())
    tree[a].append(b)
    tree[b].append(a)
#rint(tree)

depth = [-1] * (N + 1)
queue = {1}
d = 0
while queue:
    new_queue = set()
    for q in queue:
        depth[q] = d
        for v in tree[q]:
            if depth[v] == -1:
                new_queue.add(v)
    queue = new_queue
    d += 1

#print(depth)
for _ in range(Q):
    c, d = map(int, input().split())
    length = depth[d] + depth[c]
    if length % 2 == 0:
        print("Town")
    else:
        print("Road")
