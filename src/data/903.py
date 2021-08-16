n, q = [0] * 2
a = []
b = []
c = []
d = []


def format_input(filename=None):
    global n, q
    global a, b, c, d
    if filename == None:
        n, q = list(map(int, input().split()))
        ab = [list(map(int, input().split())) for i in range(n - 1)]
        for i in ab:
            a.append(i[0])
            b.append(i[1])
        cd = [list(map(int, input().split())) for i in range(q)]
        for i in cd:
            c.append(i[0])
            d.append(i[1])

    elif filename == '__random__':
        from random import randint as rng
        n = rng(2, 10**5)
        q = rng(1, 10**5)
        a = [rng(1, n - 1) for i in range(n - 1)]
        b = [rng(a[i], n) for i in range(n - 1)]
        c = [rng(1, n - 1) for i in range(q)]
        d = [rng(c[i], n) for i in range(q)]
        print(n, q)
        [print(a[i], b[i]) for i in range(n - 1)]
        [print(c[i], d[i]) for i in range(q)]


def get_answer():
    answer = []

    road = [[] for i in range(n + 1)]
    for i in range(n - 1):
        road[a[i]].append(b[i])
        road[b[i]].append(a[i])

    depth = [0] * (n + 1)

    stack = []
    for i in road[1]:
        stack.append((i, 1))
    visited = {1}

    while len(stack) > 0:
        next = stack.pop()
        if next[0] in visited:
            continue

        depth[next[0]] = next[1]
        visited.add(next[0])

        for i in road[next[0]]:
            stack.append((i, next[1] + 1))

    for i in range(q):
        if depth[c[i]] % 2 == depth[d[i]] % 2:
            answer.append('Town')
        else:
            answer.append('Road')

    return answer


if __name__ == '__main__':
    format_input()

    ans = get_answer()
    [print(i) for i in ans]
