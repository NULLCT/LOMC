def main():
    N, Q = map(int, input().split())
    L = [[] for i in range(N + 1)]
    X = [0 for i in range(N + 1)]
    for i in range(N - 1):
        a, b = map(int, input().split())
        L[a].append(b)
        L[b].append(a)

    NEXT = [1]
    CAN = [True for i in range(N + 1)]
    CAN[1] = False
    while (len(NEXT) > 0):
        NOW = NEXT
        NEXT = []
        for a in NOW:
            x = (X[a] + 1) % 2
            for b in L[a]:
                if CAN[b]:
                    X[b] = x
                    CAN[b] = False
                    NEXT.append(b)

    for q in range(Q):
        c, d = map(int, input().split())
        ans = 'Road'
        if X[c] == X[d]:
            ans = 'Town'

        print(ans)


if __name__ == '__main__':
    main()
