def inp(to_int=True):
    if not type(to_int) == bool:
        raise Exception()
    l = input().split()
    return list(map(lambda x: int(x), l)) if to_int else l


def inps(n, to_int=True):
    if not type(n) == int:
        raise Exception()
    return [inp(to_int) for _ in [0] * n]


def main():
    from collections import deque

    n, q = inp()
    to = [[] for _ in range(n)]
    for _ in range(n - 1):
        a, b = inp()
        a -= 1
        b -= 1
        to[a].append(b)
        to[b].append(a)

    cdl = []
    for _ in range(q):
        c, d = inp()
        c -= 1
        d -= 1
        cdl.append([c, d])

    dist = [-1] * n
    dist[0] = 0

    dq = deque()
    dq.append(0)

    while dq:
        v = dq.popleft()
        for j in to[v]:
            if dist[j] != -1:
                continue

            dist[j] = dist[v] + 1
            dq.append(j)

    for i in range(q):
        c, d = cdl[i]
        if (dist[c] + dist[d]) % 2 == 1:
            print('Road')
        else:
            print('Town')


if __name__ == '__main__':
    main()
