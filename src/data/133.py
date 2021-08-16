from collections import deque


def main():
    N, nQ = list(map(int, input().split()))
    E = [[] for _ in range(N)]
    for _ in range(N - 1):
        a, b = list(map(int, input().split()))
        a -= 1
        b -= 1
        E[a].append(b)
        E[b].append(a)

    def bfs(s, E):
        Q = deque()
        Q.append(s)
        visited = set()
        visited.add(s)
        dist = {}
        dist[s] = 0
        while len(Q) > 0:
            i = Q.popleft()
            for j in E[i]:
                if j in visited:
                    continue
                dist[j] = dist[i] + 1
                visited.add(j)
                Q.append(j)
        return dist

    dist = bfs(0, E)

    for _ in range(nQ):
        c, d = list(map(int, input().split()))
        c -= 1
        d -= 1
        if (dist[c] + dist[d]) % 2 == 0:
            print("Town")
        else:
            print("Road")


main()
