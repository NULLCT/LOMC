from typing import Deque


def solve_a():
    a, b = map(int, input().split())
    print(max(0, b - a + 1))


def solve_a_2nd():
    pass


def solve_b():
    n, x = map(int, input().split())
    a = map(int, input().split())
    print(['No', 'Yes'][x >= sum(a) - n // 2])


def solve_b_2nd():
    pass


def solve_c():
    n = map(int, input().split())
    c = sorted(map(int, input().split()))
    ans = 1
    for i, ci in enumerate(c):
        ans *= (ci - i)
        ans = min(ans, ans % (10**9 + 7))
    print(ans)


def solve_c_2nd():
    pass


def solve_d():
    n, q = map(int, input().split())
    nodes = [[] for _ in range(n + 1)]

    for _ in range(n - 1):
        a, b = map(int, input().split())
        nodes[a] += [b]
        nodes[b] += [a]

    bw = [-1] * (n + 1)
    bw[1] = 1
    stack = Deque([1])
    while (len(stack) != 0):
        now = stack.popleft()
        for child in nodes[now]:
            if (bw[child] == -1):
                bw[child] = (bw[now] + 1) % 2
                stack.append(child)

    for _ in range(q):
        c, d = map(int, input().split())
        if (bw[c] != bw[d]):
            print('Road')
        else:
            print('Town')


if __name__ == '__main__':
    # solve_a()
    # solve_b()
    # solve_c()
    solve_d()
    # solve_a_2nd()
    # solve_b_2nd()
    # solve_c_2nd()
