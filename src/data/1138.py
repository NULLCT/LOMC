def main():
    #n=int(input())
    #a,b=map(int,input().split())
    #a=list(map(int,input().split()))
    #a=[list(map(int,input().split())) for _ in range(h)]
    from collections import deque
    n, Q = map(int, input().split())
    ab = [[] * n for _ in range(n)]
    color = [0] * n
    for i in range(n - 1):
        a, b = map(int, input().split())
        ab[a - 1].append(b - 1)
        ab[b - 1].append(a - 1)
    q = deque()
    q.append([0, 1])
    while q:
        pos, col = q.popleft()
        color[pos] = col
        col *= -1
        for nx in ab[pos]:
            if color[nx] != 0:
                continue
            q.append([nx, col])
    for i in range(Q):
        c, d = map(int, input().split())
        if color[c - 1] == color[d - 1]:
            print('Town')
        else:
            print('Road')


if __name__ == '__main__':
    main()
