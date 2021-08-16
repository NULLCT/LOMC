from collections import deque

N, Q = map(int, input().split())
h = [[] for _ in range(N)]
for i in range(N - 1):
    a, b = map(int, input().split())
    a, b = a - 1, b - 1
    #m[a][b],m[b][a] = 1,1
    h[a].append(b)
    h[b].append(a)


def main():
    q = deque()
    q.append(0)
    tree = [-1] * N
    tree[0] = 0
    while len(q) != 0:
        x = q.popleft()
        for y in h[x]:
            if tree[y] == -1:
                tree[y] = tree[x] + 1
                q.append(y)
    #print(tree)
    for i in range(Q):
        s, g = map(int, input().split())
        s, g = s - 1, g - 1
        if (tree[s] + tree[g]) % 2 != 1:
            print("Town")
        else:
            print("Road")
    pass


if __name__ == "__main__":
    main()
