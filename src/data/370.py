from collections import deque


def solve(N, Q, ab, c, d):
    deplist = [-1] * (N + 1)
    deplist[1] = 0

    de = deque()
    de.append((1, 0))

    dpnode = 1
    dpt = 1
    while de:
        (v, dep) = de.popleft()
        for i in ab[v]:
            if deplist[i] != -1:
                continue
            deplist[i] = dep + 1
            de.append((i, dep + 1))

    for que in range(Q):
        if (deplist[c[que]] + deplist[d[que]]) % 2 == 0:
            print("Town")
        else:
            print("Road")


def main():
    N, Q = map(int, input().split())
    ab = [[] for _ in range(N + 1)]
    c = [None for _ in range(Q)]
    d = [None for _ in range(Q)]
    for _ in range(N - 1):
        a, b = map(int, input().split())
        ab[a].append(b)
        ab[b].append(a)
    for i in range(Q):
        c[i], d[i] = map(int, input().split())
    solve(N, Q, ab, c, d)


if __name__ == '__main__':
    main()
