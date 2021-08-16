#
import sys, math

sys.setrecursionlimit(10**8)


def readline():
    return sys.stdin.buffer.readline()


def read():
    return sys.stdin.buffer.read()


def decode(s):
    return s.decode()


mod = 10**9 + 7
INF = 1 << 50


def get_dist(to):
    dists = [-1] * len(to)

    def dfs(c):
        nval = dists[c] + 1
        for nc in to[c]:
            if dists[nc] == -1:
                dists[nc] = nval
                dfs(nc)

    dists[1] = 0
    dfs(1)
    return dists


def main():
    N, Q = map(int, readline().split())
    to = [[] for _ in range(N + 1)]
    for _ in range(N - 1):
        a, b = map(int, readline().split())
        to[a].append(b)
        to[b].append(a)
    D = get_dist(to)
    for _ in range(Q):
        c, d = map(int, readline().split())
        d = abs(D[c] - D[d])
        if not d % 2:
            print('Town')
        else:
            print('Road')


if __name__ == '__main__':
    main()
