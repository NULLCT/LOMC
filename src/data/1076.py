import sys
import numpy as np
from numba import njit, i8

read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines


def from_read(dtype=np.int64):
    return np.fromstring(read().decode(), dtype=dtype, sep=' ')


def from_readline(dtype=np.int64):
    return np.fromstring(readline().decode(), dtype=dtype, sep=' ')


def to_undirected(E, edge):
    G = np.vstack((E, E))
    G[edge:, 0] = G[:edge, 1]
    G[edge:, 1] = G[:edge, 0]
    key = G[:, 0] << 32 | G[:, 1]
    idx = np.argsort(key, kind="mergesort")
    return G[idx]


@njit
def euler_tour(N, G, root=1):
    assert len(G) == N + N - 2
    id = np.searchsorted(G[:, 0], np.arange(N + 2))
    parent = np.zeros(N + 1, np.int64)
    depth = np.zeros(N + 1, np.int64)
    stack, s = np.zeros(N + N, np.int64), 0
    stack[s], s = -root, s + 1
    stack[s], s = root, s + 1
    for i in range(N + N):
        v, s = stack[s - 1], s - 1
        if v < 0:
            continue
        for e in range(id[v + 1] - 1, id[v] - 1, -1):
            _, w = G[e, :2]
            if w == parent[v]: continue
            stack[s], s = -w, s + 1
            stack[s], s = w, s + 1
            parent[w] = v
            depth[w] = depth[v] + 1
    return parent, depth


@njit((i8, i8, i8[:, :], i8[:, :]), cache=True)
def solve(N, Q, G, query):
    parent, depth = euler_tour(N, G)
    doubling = np.zeros((20, N + 1), np.int64)
    doubling[0] = parent
    for i in range(20 - 1):
        for j in range(1, N + 1):
            doubling[i + 1, j] = doubling[i, doubling[i, j]]
    res = np.zeros(Q, np.int8)
    for q in range(Q):
        c, d = query[q]
        if depth[c] > depth[d]:
            c, d = d, c
        d1 = depth[c]
        d2 = depth[d]
        dd = d2 - d1
        for i in range(20):
            if (dd >> i) == 0: break
            if (dd >> i) & 1:
                d = doubling[i, d]
        if c == d:
            lca = c
        else:
            for i in range(20 - 1, -1, -1):
                if doubling[i, c] != doubling[i, d]:
                    c = doubling[i, c]
                    d = doubling[i, d]
            lca = parent[c]
        dist = d1 + d2 - 2 * depth[lca]
        if dist % 2 == 1: res[q] |= 1
    return res


def main():
    N, Q = from_readline()
    X = from_read()
    E = X[:N + N - 2].reshape(N - 1, 2)
    G = to_undirected(E, N - 1)
    query = X[N + N - 2:].reshape(Q, 2)
    res = solve(N, Q, G, query)
    for q in range(Q):
        if res[q]:
            print("Road")
        else:
            print("Town")


if __name__ == "__main__":
    main()
