import sys
from collections import deque

input = lambda: sys.stdin.readline().rstrip()


def main():
    N, Q = map(int, input().split())
    M = N - 1
    G = [[] for _ in range(N)]
    for _ in range(M):
        a, b = map(int, input().split())
        a -= 1
        b -= 1
        G[a].append([b, 1])
        G[b].append([a, 1])

    seen = [-1] * N
    que = deque()
    que.append(0)
    while que:
        k = que.popleft()
        for next in G[k]:
            j = next[0]
            if seen[j] != -1:
                continue
            seen[j] = 1 - seen[k]
            que.append(j)

    for _ in range(Q):
        c, d = map(int, input().split())
        c -= 1
        d -= 1
        if seen[c] == seen[d]:
            print('Town')
        else:
            print('Road')


if __name__ == '__main__':
    main()
