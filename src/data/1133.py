from collections import deque

N, Q = map(int, input().split())
AB = [list(map(int, input().split())) for _ in range(N - 1)]
CD = [list(map(int, input().split())) for _ in range(Q)]
root = [[] for _ in range(N)]
for a, b in AB:
    a, b = a - 1, b - 1
    root[a].append(b)
    root[b].append(a)

dists = [-1] * N
dists[0] = 0
stack = deque([0])
while len(stack):
    now = stack.popleft()
    for i in root[now]:
        if dists[i] == -1:
            dists[i] = dists[now] + 1
            stack.append(i)

for c, d in CD:
    c, d = c - 1, d - 1
    if abs(dists[c] - dists[d]) % 2:
        print('Road')
    else:
        print('Town')
