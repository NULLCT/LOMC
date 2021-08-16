from collections import deque

N, Q = map(int, input().split())
tree = [[] for i in range(N)]
d2one = [0 for i in range(N)]
is_visited = [False for i in range(N)]
for i in range(N - 1):
    ai, bi = map(int, input().split())
    ai = ai - 1
    bi = bi - 1
    tree[ai] += [bi]
    tree[bi] += [ai]

queue = deque()
queue.append((0, 0))
is_visited[0] = True

while queue:
    node, d = queue.popleft()
    d2one[node] = d
    for to_node in tree[node]:
        if not is_visited[to_node]:
            queue.append((to_node, d + 1))
            is_visited[to_node] = True

for i in range(Q):
    ci, di = map(int, input().split())
    ci = ci - 1
    di = di - 1
    if d2one[ci] % 2 == d2one[di] % 2:
        print("Town")
    else:
        print("Road")
