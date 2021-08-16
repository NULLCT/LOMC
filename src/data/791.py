from math import ceil, log2
import sys


def read():
    return sys.stdin.readline().rstrip()


def main():
    n, q = map(int, read().split())
    al = [[] for _ in range(n)]

    for _ in range(n - 1):
        a, b = [int(i) - 1 for i in read().split()]
        al[a].append(b)
        al[b].append(a)
    euler_tour = []
    depth = [0] * n
    todo = [(~0, 0), (0, 0)]
    seen = [False] * n
    while todo:
        v, d = todo.pop()
        if v >= 0:
            seen[v] = True
            depth[v] = d
            euler_tour.append((v, d))
            for u in al[v][::-1]:
                if not seen[u]:
                    todo.append((~u, d + 1))
                    todo.append((u, d + 1))
        else:
            euler_tour.append((~v, d))
    first_appear = [-1] * n
    for i, (v, _) in enumerate(euler_tour):
        if first_appear[v] < 0:
            first_appear[v] = i

    m = ceil(log2(2 * n))
    sparse_table = [[10**9] * m for _ in range(2 * n)]
    for i in range(2 * n):
        sparse_table[i][0] = euler_tour[i][1]
    for k in range(m - 1):
        for i in range(2 * n):
            sparse_table[i][k + 1] = sparse_table[i][k]
            if i + 2**k < 2 * n:
                sparse_table[i][k + 1] = min(sparse_table[i + 2**k][k],
                                             sparse_table[i][k + 1])

    for _ in range(q):
        c, d = [int(i) - 1 for i in read().split()]
        i, j = sorted([first_appear[c], first_appear[d]])
        k = int(log2(j - i))
        dlca = min(sparse_table[i][k], sparse_table[j - 2**k + 1][k])
        print(["Town", "Road"][(depth[c] + depth[d] - 2 * dlca) % 2])


if __name__ == '__main__':
    main()
