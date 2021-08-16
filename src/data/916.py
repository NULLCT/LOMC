from random import randrange
import sys
from scipy.sparse.csgraph import dijkstra
from scipy.sparse import csr_matrix


def resolve(input):
    N, Q = map(int, input().split())
    ab = [list(map(int, input().split())) for _ in range(N - 1)]
    cd = [list(map(int, input().split())) for _ in range(Q)]

    g = csr_matrix(
        ([1] * (N - 1), ([x[0] - 1 for x in ab], [x[1] - 1 for x in ab])),
        shape=(N, N))
    r = dijkstra(g, directed=False, indices=0)

    for c, d in cd:
        c -= 1
        d -= 1
        if abs(r[c] - r[d]) % 2 == 0:
            print('Town')
        else:
            print('Road')


if __name__ == '__main__':
    stdin = sys.stdin.readline

    resolve(stdin)
