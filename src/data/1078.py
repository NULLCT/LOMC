from collections import deque


def main():
    TOWN = "Town"
    ROAD = "Road"

    N, Q = map(int, input().split())
    e = [set() for _ in range(N)]

    for _ in range(N - 1):
        A, B = map(int, input().split())
        e[A - 1].add(B - 1)
        e[B - 1].add(A - 1)

    q = deque([0])
    color = [-1] * N
    color[0] = 0

    while q:
        v = q.popleft()

        for i in e[v]:
            if color[i] < 0:
                color[i] = color[v] ^ 1
                q.append(i)

    ans = []
    for _ in range(Q):
        C, D = map(int, input().split())
        if color[C - 1] == color[D - 1]:
            ans.append(TOWN)
        else:
            ans.append(ROAD)

    print(*ans, sep="\n")


if __name__ == "__main__":
    main()
