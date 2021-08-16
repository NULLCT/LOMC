from collections import deque

N, Q = map(int, input().split())
edges = [set() for _ in range(N + 1)]
for _ in range(N - 1):
    a, b = map(int, input().split())
    edges[a].add(b)
    edges[b].add(a)

nums = [None] * (N + 1)
nums[1] = 0
queue = deque()
queue.append((1, 0))
done = {1}
while queue:
    cur, num = queue.popleft()
    nums[cur] = num
    for n in edges[cur]:
        if n in done:
            continue
        queue.append((n, 1 - num))
        done.add(n)

for _ in range(Q):
    c, d = map(int, input().split())
    print('Town' if nums[c] == nums[d] else 'Road')
