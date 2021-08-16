import sys
from collections import deque


def Main():
    N, Q = map(int, sys.stdin.readline().strip().split())
    grid = [[] for _ in range(N)]
    for _ in range(N - 1):
        a, b = map(int, sys.stdin.readline().strip().split())
        grid[a - 1].append(b - 1)
        grid[b - 1].append(a - 1)
    que = deque([0])
    seen = [-1] * N
    seen[0] = 0
    while que:
        v = que.popleft()
        for i in grid[v]:
            if seen[i] == -1:
                seen[i] = 1 - seen[v]
                que.append(i)
    for _ in range(Q):
        c, d = map(int, sys.stdin.readline().strip().split())
        if seen[c - 1] == seen[d - 1]:
            print('Town')
        else:
            print('Road')


if __name__ == '__main__':
    Main()
