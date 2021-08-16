import sys
import numpy as np
#from numba import njit, b1, i1, i4, i8, f8 #, jitclass,
sys.setrecursionlimit(10**9)

read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines


def input():
    return sys.stdin.readline().strip()


def from_read(dtype=np.int64):
    return np.fromstring(read().decode(), dtype=dtype, sep=' ')


def from_readline(dtype=np.int64):
    return np.fromstring(readline().decode(), dtype=dtype, sep=' ')


#@njit("(i8,i8,i8[:,:],)", cache=True)
def main(N, Q, A, B, C, D):
    repn = [[] for _ in range(N)]
    for a, b in zip(A, B):
        repn[a].append(b)
        repn[b].append(a)

    depth = [0] * N

    def dfs(v, p=-1):
        for nv in repn[v]:
            if nv == p: continue
            depth[nv] = depth[v] + 1
            dfs(nv, v)

    dfs(0)
    for c, d in zip(C, D):
        dist = (depth[c] + depth[d]) % 2
        print('Town' if dist % 2 == 0 else 'Road')


if __name__ == '__main__':
    N, Q = from_readline()
    inp = from_read()
    A, B = inp[:(N - 1) * 2].reshape(N - 1, 2).T
    C, D = inp[(N - 1) * 2:].reshape(Q, 2).T
    main(N, Q, A - 1, B - 1, C - 1, D - 1)
