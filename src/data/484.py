from collections import deque


def main():
    N, Q = map(int, input().split())
    g = [[] for _ in range(N)]

    for _ in range(N - 1):
        A, B = map(int, input().split())
        A -= 1
        B -= 1
        g[A].append(B)
        g[B].append(A)

    q = deque()
    q.append(0)
    dist = [-1] * N
    dist[0] = 0

    while q:
        now = q.popleft()

        for nxt in g[now]:
            if dist[nxt] == -1:
                dist[nxt] = dist[now] + 1
                q.append(nxt)

    for _ in range(Q):
        C, D = map(int, input().split())
        C -= 1
        D -= 1

        if (dist[C] + dist[D]) % 2 == 0:
            print("Town")
        else:
            print("Road")


main()
