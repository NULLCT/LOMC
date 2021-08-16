def main():
    import sys
    input = sys.stdin.readline
    from collections import deque
    N, Q = map(int, input().split())
    connect = [list() for _ in range(N)]
    for _ in range(N - 1):
        a, b = map(int, input().split())
        connect[a - 1].append(b - 1)
        connect[b - 1].append(a - 1)
    distance = [-1] * N
    q = deque()
    q.append((0, 0))
    while q:
        now = q.popleft()
        now_pos, distance_from_zero = now
        distance[now_pos] = distance_from_zero
        for nxt in connect[now_pos]:
            if distance[nxt] > -1:
                continue
            q.append((nxt, distance_from_zero + 1))
    #print(distance)
    for _ in range(Q):
        c, d = map(int, input().split())
        dis = distance[c - 1] + distance[d - 1]
        if dis % 2 == 0:
            print("Town")
        else:
            print("Road")


if __name__ == "__main__":
    main()
