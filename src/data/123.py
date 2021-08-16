import sys

sys.setrecursionlimit(10**7)

mod = 998244353


def bfs():
    while len(que) > 0:
        que_now = que.pop(0)
        for nxt in way[que_now]:
            if dist[nxt] == -1:
                que.append(nxt)
                dist[nxt] = dist[que_now] + 1


if __name__ == '__main__':
    readline = sys.stdin.readline
    read = sys.stdin.read
    N, Q = map(int, readline().split())
    way = [[] for _ in range(N)]
    for i in [0] * (N - 1):
        A, B = map(int, readline().split())
        way[A - 1].append(B - 1)
        way[B - 1].append(A - 1)
    que = [0]
    dist = [-1] * N
    dist[0] = 0
    bfs()
    # print(dist)
    for q in [0] * Q:
        c, d = map(int, readline().split())
        if (dist[c - 1] - dist[d - 1]) % 2 == 0:
            print("Town")
        else:
            print("Road")
