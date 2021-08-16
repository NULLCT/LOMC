from collections import deque

N, Q = map(int, input().split())
node = [[] for _ in range(N + 1)]
for i in range(N - 1):
    a, b = map(int, input().split())
    node[a].append(b)
    node[b].append(a)


def BFS(s):
    q = deque([])
    v = [False] * (N + 1)
    dis = [0] * (N + 1)
    color = [0] * (N + 1)
    color[s] = 1
    q.append(s)
    v[s] = True

    while q:
        x = q.popleft()
        for nx in node[x]:
            if not (v[nx]):
                dis[nx] = dis[x] + 1
                if dis[nx] % 2 == 0:
                    color[nx] = 1
                q.append(nx)
                v[nx] = True
    return dis, color


ans, color = BFS(1)

for _ in range(Q):
    c, d = map(int, input().split())
    if color[c] == color[d]:
        print('Town')
    else:
        print('Road')
