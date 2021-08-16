from collections import deque

n, q = map(int, input().split())
ab = [[] for _ in range(n)]
for i in range(n - 1):
    a, b = map(int, input().split())
    ab[a - 1].append(b - 1)
    ab[b - 1].append(a - 1)

st = deque()
st.append(0)
dist = [-1] * n
dist[0] = 0
while st:
    cur = st.popleft()
    for j in ab[cur]:
        if dist[j] != -1:
            continue
        dist[j] = dist[cur] + 1
        st.append(j)

for i in range(q):
    c, d = map(int, input().split())
    c -= 1
    d -= 1
    if (dist[c] - dist[d]) % 2 == 0:
        ans = "Town"
    else:
        ans = "Road"
    print(ans)
