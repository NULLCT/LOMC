import sys
import numpy as np


def tocsr(n, E):
    E -= 1
    m = E.shape[0]
    E = np.vstack((E, E))
    E[m:, 0] = E[:m, 1]
    E[m:, 1] = E[:m, 0]
    m = E.shape[0]
    indices, indptr = np.empty(m, np.int64), np.zeros(n + 1, np.int64)
    for e in E[:, 0]:
        indptr[e + 1] += 1
    indptr = indptr.cumsum()
    cnt = indptr.copy()
    for i in range(m):
        e0, e1 = E[i]
        indices[cnt[e0]] = e1
        cnt[e0] += 1
    return indices, indptr


def solve(E, Q):
    Q -= 1
    n = E.shape[0] + 1
    indices, indptr = tocsr(n, E)
    dist = np.full(n, -1, np.int64)
    q = np.empty(2 * n, np.int64)
    head, tail = 0, 1
    q[0] = 0
    while head < tail:
        x = q[head]
        head += 1
        for i in range(indptr[x], indptr[x + 1]):
            y = indices[i]
            if dist[y] >= 0: continue
            dist[y] = dist[x] + 1
            q[tail] = y
            tail += 1
    q = Q.shape[0]
    ans = np.empty(q, np.bool_)
    for i in range(q):
        c, d = Q[i]
        ans[i] = (dist[c] - dist[d]) % 2 == 0
    return ans


def main():
    n, q = map(int, input().split())
    IN = np.fromstring(sys.stdin.read(), np.int64, sep=' ').reshape(-1, 2)
    E = IN[:n - 1]
    Q = IN[n - 1:]
    ans = np.where(solve(E, Q), 'Town', 'Road')
    print('\n'.join(ans.tolist()))


if __name__ == '__main__':
    if sys.argv[-1] == 'ONLINE_JUDGE':
        from numba.pycc import CC
        from numba import njit
        cc = CC('my_module')
        funcs_and_sigs = [('tocsr', 'UniTuple(i8[:], 2)(i8, i8[:,:])'),
                          ('solve', 'b1[:](i8[:,:], i8[:,:])')]
        d = globals()
        for fname, sig in funcs_and_sigs:
            func = d[fname]
            cc.export(func.__name__, sig)(func)
            d[fname] = njit(func)
        cc.compile()
        exit()
    from my_module import *
    main()
