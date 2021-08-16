N, Q = map(int, input().split())

e_list = [[] for _ in range(N)]

for i in range(N - 1):
    a, b = map(int, input().split())
    e_list[a - 1].append(b - 1)
    e_list[b - 1].append(a - 1)

from collections import deque


def dijkstra(N, s, e_list):
    done = [False for _ in range(N)]
    dist = [0 for _ in range(N)]  #1なら間の辺の数は偶数

    d = deque()

    d.append(s)

    while d:
        cur_node = d.popleft()
        for e in e_list[cur_node]:
            if done[e] == False:
                done[e] = True
                dist[e] = dist[cur_node] + 1
                d.append(e)
    return dist


res = dijkstra(N, 0, e_list)
for i in range(Q):
    c, d = map(int, input().split())
    if (res[c - 1] - res[d - 1]) % 2 == 0:
        print("Town")
    else:
        print("Road")
