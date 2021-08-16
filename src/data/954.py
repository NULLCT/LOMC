from collections import deque

N, Q = list(map(int, input().split()))

K = [[] for _ in range(N + 1)]
nums = [float("inf") for _ in range(N + 1)]

for _ in range(N - 1):
    a, b = map(int, input().split())
    K[a].append(b)
    K[b].append(a)


def bfs(now, parent):
    que = deque()
    que.append((now, parent))

    while que:
        now, parent = que.popleft()
        for i in K[now]:
            if nums[i] == float("inf"):
                nums[i] = nums[now] + 1
                que.append((i, now))


nums[1] = 0
bfs(1, 0)

for _ in range(Q):
    c, d = map(int, input().split())
    cd = nums[c] - nums[d]
    if cd % 2 == 0:
        print("Town")
    else:
        print("Road")
