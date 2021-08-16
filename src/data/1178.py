import sys

sys.setrecursionlimit(10**7)

read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines


def main():
    N, Q = map(int, input().split())
    AB = [list(map(int, input().split())) for _ in range(N - 1)]
    CD = [list(map(int, input().split())) for _ in range(Q)]

    PATH = [[] for _ in range(N + 1)]
    for a, b in AB:
        PATH[a].append(b)
        PATH[b].append(a)

    POS = [True] * (N + 1)
    q = [(1, True, -1)]
    while q:
        u, t, parent = q.pop()
        for v in PATH[u]:
            if v == parent:
                continue

            POS[v] = not (t)
            q.append((v, not (t), u))

    # print(POS)

    ans = []
    for c, d in CD:
        if POS[c] == POS[d]:
            ans.append("Town")
        else:
            ans.append("Road")

    print("\n".join(ans))

    return


if __name__ == "__main__":
    main()
