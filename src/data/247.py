import sys

input = sys.stdin.readline  # "\n"を含む


def solve(N, Q, Edge, Query):
    L = [[] * (N + 1) for _ in range(N + 1)]
    for a, b in Edge:
        L[a].append(b)
        L[b].append(a)

    Group = [0] * (N + 1)

    def dfs(start=1):
        par = [-1] * (N + 1)
        stack = [start]

        while stack:
            u = stack.pop()
            p = par[u]
            temp = Group[u] ^ 1
            for v in L[u]:
                if v == p: continue
                par[v] = u
                Group[v] = temp
                if len(L[v]) != 1:
                    stack.append(v)

    dfs()

    res = []
    for c, d in Query:
        if Group[c] == Group[d]:
            res.append("Town")
        else:
            res.append("Road")

    return res


def main():
    N, Q = map(int, input().split())
    Edge = [tuple(map(int, input().split())) for _ in range(N - 1)]
    Query = [tuple(map(int, input().split())) for _ in range(Q)]
    res = solve(N, Q, Edge, Query)
    print(*res, sep="\n")


if __name__ == "__main__":
    main()
