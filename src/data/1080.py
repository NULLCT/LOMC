import collections


def main():

    N, Q = map(int, input().split())
    tree = collections.defaultdict(set)
    for _ in range(N - 1):
        a, b = map(int, input().split())
        a -= 1
        b -= 1
        tree[a].add(b)
        tree[b].add(a)
    # print(tree)

    dist = dict()
    dist[0] = 0
    cur = [0]
    visited = [0 for _ in range(N)]
    visited[0] = 1
    d = 0
    while cur:
        tmp = []
        d += 1
        for a in cur:
            for b in tree[a]:
                if visited[b] == 0:
                    visited[b] = 1
                    tmp.append(b)
                    dist[b] = d
        cur = tmp

    # print(dist)

    for _ in range(Q):
        c, d = map(int, input().split())
        c -= 1
        d -= 1
        u = dist[c] - dist[d]
        if u % 2 == 0:
            print('Town')
        else:
            print('Road')


if __name__ == '__main__':
    main()
