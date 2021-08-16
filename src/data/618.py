import sys
import math
from collections import deque

sys.setrecursionlimit(10**6)
INF = float('inf')


def solve():
    N, Q = map(int, input().split())

    graph = [[] for _ in range(N)]
    for _ in range(N - 1):
        a, b = map(int, input().split())
        a -= 1
        b -= 1
        graph[a].append(b)
        graph[b].append(a)

    visited = [False] * N
    is_red = [False] * N

    deq = deque()
    deq.append(0)
    while len(deq) != 0:
        cur = deq.popleft()
        visited[cur] = True
        for next in graph[cur]:
            if visited[next]:
                continue
            deq.append(next)
            if not is_red[cur]:
                is_red[next] = True
    ans = []
    for _ in range(Q):
        c, d = map(int, input().split())
        c -= 1
        d -= 1
        if is_red[c] == is_red[d]:
            ans.append('Town')
        else:
            ans.append('Road')

    print(*ans, sep='\n')


if __name__ == '__main__':
    solve()
