import sys
from collections import deque


def main():
    N, Q = map(int, input().split())
    graph = [[] for _ in range(N)]
    # M辺の情報
    for m in range(N - 1):
        a, b = map(int, input().split())
        # 頂点が0始まりで無ければ、1を引く
        graph[a - 1].append(b - 1)
        graph[b - 1].append(a - 1)
    dist = [-1 for _ in range(N)]  # 最短距離
    dist[0] = 0

    to_visit = deque()
    to_visit.append(0)

    while to_visit:
        old_v = to_visit.popleft()
        for new_v in graph[old_v]:
            if dist[new_v] == -1:
                dist[new_v] = 1 - dist[old_v]
                to_visit.append(new_v)

    for q in range(Q):
        c, d = map(int, input().split())
        c -= 1
        d -= 1
        if dist[c] == dist[d]:
            print('Town')
        else:
            print('Road')


if __name__ == '__main__':
    main()
