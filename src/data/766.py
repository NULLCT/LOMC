from collections import deque


def bfs(edges, N):
    inf = float("inf")
    waiting = deque()
    done = [0] * N
    done[0] = 2
    dist = [inf] * N
    dist[0] = 0
    for n in edges[0]:
        done[n] = 1
        waiting.append(n)
        dist[n] = 1
    while (len(waiting)):
        cur_node = waiting.popleft()
        if (done[cur_node] != 2):
            done[cur_node] = 2
            for n in edges[cur_node]:
                if (done[n] != 2):
                    done[n] = 1
                    dist[n] = dist[cur_node] + 1
                    waiting.append(n)
    return dist


N, Q = map(int, input().split())
e_list = [[] for i in range(N)]
for i in range(N - 1):
    a, b = map(int, input().split())
    e_list[a - 1].append(b - 1)
    e_list[b - 1].append(a - 1)

dist = bfs(e_list, N)

for i in range(Q):
    c, d = map(int, input().split())
    if (abs(dist[c - 1] - dist[d - 1]) % 2 == 0):
        print("Town")
    else:
        print("Road")
