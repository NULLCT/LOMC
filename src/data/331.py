N, Q = list(map(int, input().split()))
AB = [[None, None] for i in range(N - 1)]
Node = [[] for i in range(N)]


def WFS():
    St = [0] * N
    Q = {0}
    Q1 = set()
    i = 1
    while Q:
        Q1.clear()
        Q1 |= Q
        for q in Q:
            if St[q] == 0:
                if i % 2 == 1:
                    St[q] = 1
                else:
                    St[q] = 2

                Q1.remove(q)
                Q1 |= set(Node[q])
            else:
                Q1.remove(q)
        i += 1
        Q.clear()
        Q |= Q1
    return St


for i in range(N - 1):
    AB[i] = list(map(int, input().split()))
    Node[AB[i][0] - 1].append(AB[i][1] - 1)
    Node[AB[i][1] - 1].append(AB[i][0] - 1)

D = WFS()
ans = [0] * Q

for i in range(Q):
    c, d = list(map(int, input().split()))
    if D[c - 1] == D[d - 1]:
        ans[i] = 0
    else:
        ans[i] = 1

for i in range(Q):
    if ans[i] % 2 == 0:
        print("Town")
    else:
        print("Road")
