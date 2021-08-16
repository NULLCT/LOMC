import sys
from collections import deque


def _s():
    return sys.stdin.readline().strip()


def _sa():
    return sys.stdin.readline().strip().split()


def _i():
    return int(sys.stdin.readline().strip())


def _ia():
    return map(int, sys.stdin.readline().strip().split())


def main():
    N, Q = _ia()
    EDGE = [[] for _ in range(N)]
    for _ in range(N - 1):
        ai, bi = _ia()
        EDGE[ai - 1].append(bi - 1)
        EDGE[bi - 1].append(ai - 1)

    walk = [-1] * N
    q = deque([[0, 0]])
    while q:
        p, cnt = q.popleft()
        if walk[p] >= 0:
            continue
        walk[p] = cnt % 2
        cnt1 = cnt + 1
        for nxt in EDGE[p]:
            q.append([nxt, cnt1])

    for _ in range(Q):
        ci, di = _ia()
        if walk[ci - 1] == walk[di - 1]:
            print("Town")
        else:
            print("Road")


if __name__ == "__main__":
    main()
