def q4():
    N, Q = [int(x) for x in input().split()]
    ABs = [[int(x) for x in input().split()] for _ in range(N - 1)]
    Qs = [[int(x) for x in input().split()] for _ in range(Q)]
    nodes = {
        i + 1: {
            'index': i + 1,
            'is_searched': False,
            'length': 0,
            'children': [],
            'degree': 0
        }
        for i in range(N)
    }
    for a, b in ABs:
        nodes[a]['children'].append(b)
        nodes[b]['children'].append(a)
        nodes[a]['degree'] = nodes[a]['degree'] + 1
        nodes[b]['degree'] = nodes[b]['degree'] + 1
    for i, node in nodes.items():
        if node['degree'] == 1:
            start_index = node['index']
            break
    answer = 0
    from collections import deque
    d = deque()
    d.append(start_index)
    nodes[start_index]['is_searched'] = True
    nodes[start_index]['length'] = 0
    while d:
        n = d.popleft()
        children = nodes[n]['children']
        for c in children:
            if not nodes[c]['is_searched']:
                d.append(c)
                nodes[c]['is_searched'] = True
                nodes[c]['length'] = nodes[n]['length'] + 1
    for c, d in Qs:
        x = abs(nodes[c]['length'] - nodes[d]['length'])
        if x % 2 == 1:
            answer = 'Road'
        else:
            answer = 'Town'
        print(answer)


q4()
