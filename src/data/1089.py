import sys
from heapq import *
import numpy as np
import numba
from numba import njit, b1, i1, i4, i8, f8

read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines


def from_read(dtype=np.int64):
    return np.fromstring(read().decode(), dtype=dtype, sep=' ')


def from_readline(dtype=np.int64):
    return np.fromstring(readline().decode(), dtype=dtype, sep=' ')


def to_undirected(G, add_index=False):
    N = len(G)
    if add_index:
        G = np.append(G, np.arange(N).reshape(N, 1), axis=1)
    G = np.vstack((G, G))
    G[N:, 0] = G[:N, 1]
    G[N:, 1] = G[:N, 0]
    key = G[:, 0] << 32 | G[:, 1]
    idx = np.argsort(key, kind='mergesort')
    return G[idx]


@njit
def tree_bfs(N, G, root=1):
    idx = np.searchsorted(G[:, 0], np.arange(N + 2))
    que, l, r = np.empty(N, np.int64), 0, 0
    parent = np.zeros(N + 1, np.int64)
    depth = np.zeros(N + 1, np.int64)
    que[r], r = root, r + 1
    depth[root] = 1
    for _ in range(N):
        v, l = que[l], l + 1
        for w in G[idx[v]:idx[v + 1], 1]:
            if parent[v] == w:
                continue
            parent[w] = v
            depth[w] = depth[v] + 1
            que[r], r = w, r + 1
    order = que
    return parent, order, depth


@njit((i8, i8, i8[:, :], i8[:, :]), cache=True)
def main(N, Q, G, CD):
    parent, order, depth = tree_bfs(N, G)
    for q in range(Q):
        c, d = CD[q]
        if (depth[c] + depth[d]) % 2 == 0:
            print('Town')
        else:
            print('Road')


N, Q = from_readline()
nums = from_read().reshape(N + Q - 1, 2)
G = to_undirected(nums[:N - 1])
CD = nums[N - 1:]

main(N, Q, G, CD)
