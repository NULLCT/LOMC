from collections import deque


def bfs(V, edges):
    waiting = deque()
    done = [-1] * V
    done[0] = 0
    for n in edges[0]:
        waiting.append([n, 0])
    while len(waiting):
        cur = waiting.popleft()
        cur_node = cur[0]
        cur_dist = cur[1]
        if done[cur_node] == -1:
            done[cur_node] = cur_dist + 1
            for n in edges[cur_node]:
                if done[n] == -1:
                    waiting.append([n, cur_dist + 1])
    return done


N, Q = map(int, input().split())
e_list = [[] for i in range(N)]
for i in range(N - 1):
    a, b = map(int, input().split())
    e_list[a - 1].append(b - 1)
    e_list[b - 1].append(a - 1)
dist = bfs(N, e_list)

for i in range(Q):
    c, d = map(int, input().split())
    tmp = dist[c - 1] - dist[d - 1]
    if tmp % 2 == 1:
        print("Road")
    else:
        print("Town")
