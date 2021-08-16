import sys
import collections

input = sys.stdin.readline


def main():
    n, q = map(int, input().strip().split())
    G = collections.defaultdict(list)
    for _ in range(n - 1):
        a, b = map(int, input().strip().split())
        a -= 1
        b -= 1
        G[a].append(b)
        G[b].append(a)
    D = {}
    Q = collections.deque()
    Q.append((0, 0))
    while Q:
        x, d = Q.popleft()
        if x in D:
            continue
        D[x] = d
        for y in G[x]:
            Q.append((y, d + 1))

    for query in range(q):
        a, b = map(int, input().strip().split())
        a -= 1
        b -= 1
        dist_a, dist_b = D[a], D[b]
        # print('distances', dist_a, dist_b)
        if (dist_a + dist_b) % 2 == 0:
            print('Town')
        else:
            print('Road')


main()
