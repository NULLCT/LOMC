N, Q = map(int, input().split())
edge = [[] for _ in range(N)]
for _ in range(N - 1):
    A, B = map(lambda x: int(x) - 1, input().split())
    edge[A].append(B)
    edge[B].append(A)


def kinohukasa(edge, N, i):
    hukasa = [-1] * N
    stack = [i]
    hukasa[i] = 0
    while stack:
        at = stack.pop()
        for next in edge[at]:
            if hukasa[next] == -1:
                hukasa[next] = hukasa[at] + 1
                stack.append(next)
    return hukasa


deapth = kinohukasa(edge, N, 0)
for _ in range(Q):
    c, d = map(lambda x: int(x) - 1, input().split())
    if (deapth[c] + deapth[d]) % 2 == 1:
        print("Road")
    else:
        print("Town")
