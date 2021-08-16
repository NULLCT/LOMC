from collections import deque


def lmap(func, iter):
    return list(map(func, iter))


def main():
    n, q = map(int, input().split())
    ABs = [lmap(int, input().split()) for _ in range(n - 1)]
    CDs = [lmap(int, input().split()) for _ in range(q)]

    adjs = [[] for _ in range(n)]
    for a, b in ABs:
        adjs[a - 1].append(b - 1)
        adjs[b - 1].append(a - 1)

    cols = [-1] * n
    cols[0] = 0
    q = deque([(0, 0)])
    while q:
        v, c = q.popleft()
        for vi in adjs[v]:
            if cols[vi] == -1:
                cols[vi] = (c + 1) % 2
                q.append((vi, (c + 1) % 2))

    for c, d in CDs:
        if cols[c - 1] ^ cols[d - 1]:
            print('Road')
        else:
            print('Town')


if __name__ == '__main__':
    main()
