import sys


def main():
    input = sys.stdin.readline
    N, Q = map(int, input().split())
    G = [[] for _ in range(N)]
    for _ in range(N - 1):
        a, b = map(int, input().split())
        a, b = a - 1, b - 1
        G[a].append(b)
        G[b].append(a)
    dist = [-1] * N
    stk = [0]
    dist[0] = 0
    while stk:
        v = stk.pop()
        for nv in G[v]:
            if dist[nv] >= 0: continue
            dist[nv] = dist[v] + 1
            stk.append(nv)
    for _ in range(Q):
        c, d = map(int, input().split())
        c, d = c - 1, d - 1
        if dist[c] & 1 != dist[d] & 1:
            print('Road')
        else:
            print('Town')


if __name__ == '__main__':
    main()
