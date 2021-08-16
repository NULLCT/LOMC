from collections import defaultdict

n, q = map(int, input().split())
nei_dict = defaultdict(set)
for _ in range(n - 1):
    a, b = map(int, input().split())
    a -= 1
    b -= 1
    nei_dict[a].add(b)
    nei_dict[b].add(a)

stack = [(0, -1, 0)]
max_t = -1
max_c = -1
visited = set()
while stack:
    curr_t, prev_t, curr_c = stack.pop()
    if curr_c > max_c:
        max_t = curr_t
        max_c = curr_c
    if curr_t in visited:
        continue
    visited.add(curr_t)
    for next_t in nei_dict[curr_c]:
        if next_t == prev_t:
            continue
        stack.append((next_t, curr_t, curr_c + 1))

stack = [(max_t, -1, 0)]
depth = [0 for _ in range(n)]
visited = set()
while stack:
    curr_t, prev_t, curr_d = stack.pop()
    if curr_t in visited:
        continue
    visited.add(curr_t)
    depth[curr_t] = curr_d
    for next_t in nei_dict[curr_t]:
        if next_t == prev_t:
            continue
        stack.append((next_t, curr_t, curr_d + 1))

for _ in range(q):
    c, d = map(int, input().split())
    c -= 1
    d -= 1
    if abs(depth[c] - depth[d]) % 2 == 0:
        print("Town")
    else:
        print("Road")