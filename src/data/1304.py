import bisect
import copy
import decimal
import fractions
import heapq
import itertools
import math
import random
import sys
from collections import Counter, deque, defaultdict
from functools import lru_cache, reduce
from heapq import heappush, heappop, heapify, heappushpop, _heappop_max, _heapify_max


def _heappush_max(heap, item):
    heap.append(item)
    heapq._siftdown_max(heap, 0, len(heap) - 1)


def _heappushpop_max(heap, item):
    if heap and item < heap[0]:
        item, heap[0] = heap[0], item
        heapq._siftup_max(heap, 0)
    return item


from math import gcd as GCD

read = sys.stdin.read
readline = sys.stdin.readline
readlines = sys.stdin.readlines


class Graph:
    def __init__(self,
                 V,
                 edges=False,
                 graph=False,
                 directed=False,
                 weighted=False):
        self.V = V
        self.directed = directed
        self.weighted = weighted
        if not graph:
            self.edges = edges
            self.graph = [[] for i in range(self.V)]
            if weighted:
                for i, j, d in self.edges:
                    self.graph[i].append((j, d))
                    if not self.directed:
                        self.graph[j].append((i, d))
            else:
                for i, j in self.edges:
                    self.graph[i].append(j)
                    if not self.directed:
                        self.graph[j].append(i)
        else:
            self.graph = graph
            self.edges = []
            for i in range(self.V):
                if self.weighted:
                    for j, d in self.graph[i]:
                        if self.directed or not self.directed and i <= j:
                            self.edges.append((i, j, d))
                else:
                    for j in self.graph[i]:
                        if self.directed or not self.directed and i <= j:
                            self.edges.append((i, j))

    def SS_BFS(self,
               s,
               bipartite_graph=False,
               linked_components=False,
               parents=False,
               unweighted_dist=False,
               weighted_dist=False):
        seen = [False] * self.V
        seen[s] = True
        if linked_components:
            lc = [s]
        if parents:
            ps = [None] * self.V
            ps[s] = s
        if unweighted_dist or bipartite_graph:
            uwd = [float('inf')] * self.V
            uwd[s] = 0
        if weighted_dist:
            wd = [float('inf')] * self.V
            wd[s] = 0
        queue = deque([s])
        while queue:
            x = queue.popleft()
            for y in self.graph[x]:
                if self.weighted:
                    y, d = y
                if not seen[y]:
                    seen[y] = True
                    queue.append(y)
                    if linked_components:
                        lc.append(y)
                    if parents:
                        ps[y] = x
                    if unweighted_dist or bipartite_graph:
                        uwd[y] = uwd[x] + 1
                    if weighted_dist:
                        wd[y] = wd[x] + d
        if bipartite_graph:
            bg = [[], []]
            for tpl in self.edges:
                i, j = tpl[:2] if self.weighted else tpl
                if type(uwd[i]) == float or type(uwd[j]) == float:
                    continue
                if not uwd[i] % 2 ^ uwd[j] % 2:
                    bg = False
                    break
            else:
                for x in range(self.V):
                    if type(uwd[x]) == float:
                        continue
                    bg[uwd[x] % 2].append(x)
        tpl = ()
        if bipartite_graph:
            tpl += (bg, )
        if linked_components:
            tpl += (lc, )
        if parents:
            tpl += (ps, )
        if unweighted_dist:
            tpl += (uwd, )
        if weighted_dist:
            tpl += (wd, )
        if len(tpl) == 1:
            tpl = tpl[0]
        return tpl

    def AP_BFS(self,
               bipartite_graph=False,
               linked_components=False,
               parents=False):
        seen = [False] * self.V
        if bipartite_graph:
            bg = [None] * self.V
            cnt = -1
        if linked_components:
            lc = []
        if parents:
            ps = [None] * self.V
        for s in range(self.V):
            if seen[s]:
                continue
            seen[s] = True
            if bipartite_graph:
                cnt += 1
                bg[s] = (cnt, s & 2)
            if linked_components:
                lc.append([s])
            if parents:
                ps[s] = s
            queue = deque([s])
            while queue:
                x = queue.popleft()
                for y in self.graph[x]:
                    if self.weighted:
                        y, d = y
                    if not seen[y]:
                        seen[y] = True
                        queue.append(y)
                        if bipartite_graph:
                            bg[y] = (cnt, bg[x][1] ^ 1)
                        if linked_components:
                            lc[-1].append(y)
                        if parents:
                            ps[y] = x
        if bipartite_graph:
            bg_ = bg
            bg = [[[], []] for i in range(cnt + 1)]
            for tpl in self.edges:
                i, j = tpl[:2] if self.weighted else tpl
                if not bg_[i][1] ^ bg_[j][1]:
                    bg[bg_[i][0]] = False
            for x in range(self.V):
                if bg[bg_[x][0]]:
                    bg[bg_[x][0]][bg_[x][1]].append(x)
        tpl = ()
        if bipartite_graph:
            tpl += (bg, )
        if linked_components:
            tpl += (lc, )
        if parents:
            tpl += (ps, )
        if len(tpl) == 1:
            tpl = tpl[0]
        return tpl

    def SS_DFS(self,
               s,
               bipartite_graph=False,
               cycle_detection=False,
               directed_acyclic=False,
               euler_tour=False,
               linked_components=False,
               parents=False,
               postorder=False,
               preorder=False,
               subtree_size=False,
               topological_sort=False,
               unweighted_dist=False,
               weighted_dist=False):
        seen = [False] * self.V
        finished = [False] * self.V
        if directed_acyclic or cycle_detection or topological_sort:
            dag = True
        if euler_tour:
            et = []
        if linked_components:
            lc = []
        if parents or cycle_detection or subtree_size:
            ps = [None] * self.V
            ps[s] = s
        if postorder or topological_sort:
            post = []
        if preorder:
            pre = []
        if subtree_size:
            ss = [1] * self.V
        if unweighted_dist or bipartite_graph:
            uwd = [float('inf')] * self.V
            uwd[s] = 0
        if weighted_dist:
            wd = [float('inf')] * self.V
            wd[s] = 0
        stack = [(s, 0)] if self.weighted else [s]
        while stack:
            if self.weighted:
                x, d = stack.pop()
            else:
                x = stack.pop()
            if not seen[x]:
                seen[x] = True
                stack.append((x, d) if self.weighted else x)
                if euler_tour:
                    et.append(x)
                if linked_components:
                    lc.append(x)
                if preorder:
                    pre.append(x)
                for y in self.graph[x]:
                    if self.weighted:
                        y, d = y
                    if not seen[y]:
                        stack.append((y, d) if self.weighted else y)
                        if parents or cycle_detection or subtree_size:
                            ps[y] = x
                        if unweighted_dist or bipartite_graph:
                            uwd[y] = uwd[x] + 1
                        if weighted_dist:
                            wd[y] = wd[x] + d
                    elif not finished[y]:
                        if (directed_acyclic or cycle_detection
                                or topological_sort) and dag:
                            dag = False
                            if cycle_detection:
                                cd = (y, x)
            elif not finished[x]:
                finished[x] = True
                if euler_tour:
                    et.append(~x)
                if postorder or topological_sort:
                    post.append(x)
                if subtree_size:
                    for y in self.graph[x]:
                        if y == ps[x]:
                            continue
                        ss[x] += ss[y]
        if bipartite_graph:
            bg = [[], []]
            for tpl in self.edges:
                i, j = tpl[:2] if self.weighted else tpl
                if type(uwd[i]) == float or type(uwd[j]) == float:
                    continue
                if not uwd[i] % 2 ^ uwd[j] % 2:
                    bg = False
                    break
            else:
                for x in range(self.V):
                    if type(uwd[x]) == float:
                        continue
                    bg[uwd[x] % 2].append(x)
        tpl = ()
        if bipartite_graph:
            tpl += (bg, )
        if cycle_detection:
            if dag:
                cd = []
            else:
                y, x = cd
                cd = self.Route_Restoration(y, x, ps)
            tpl += (cd, )
        if directed_acyclic:
            tpl += (dag, )
        if euler_tour:
            tpl += (et, )
        if linked_components:
            tpl += (lc, )
        if parents:
            tpl += (ps, )
        if postorder:
            tpl += (post, )
        if preorder:
            tpl += (pre, )
        if subtree_size:
            tpl += (ss, )
        if topological_sort:
            if dag:
                tp_sort = post[::-1]
            else:
                tp_sort = []
            tpl += (tp_sort, )
        if unweighted_dist:
            tpl += (uwd, )
        if weighted_dist:
            tpl += (wd, )
        if len(tpl) == 1:
            tpl = tpl[0]
        return tpl

    def AP_DFS(self,
               bipartite_graph=False,
               cycle_detection=False,
               directed_acyclic=False,
               euler_tour=False,
               linked_components=False,
               parents=False,
               postorder=False,
               preorder=False,
               topological_sort=False):
        seen = [False] * self.V
        finished = [False] * self.V
        if bipartite_graph:
            bg = [None] * self.V
            cnt = -1
        if directed_acyclic or cycle_detection or topological_sort:
            dag = True
        if euler_tour:
            et = []
        if linked_components:
            lc = []
        if parents or cycle_detection:
            ps = [None] * self.V
        if postorder or topological_sort:
            post = []
        if preorder:
            pre = []
        for s in range(self.V):
            if seen[s]:
                continue
            if bipartite_graph:
                cnt += 1
                bg[s] = (cnt, s & 2)
            if linked_components:
                lc.append([])
            if parents:
                ps[s] = s
            stack = [(s, 0)] if self.weighted else [s]
            while stack:
                if self.weighted:
                    x, d = stack.pop()
                else:
                    x = stack.pop()
                if not seen[x]:
                    seen[x] = True
                    stack.append((x, d) if self.weighted else x)
                    if euler_tour:
                        et.append(x)
                    if linked_components:
                        lc[-1].append(x)
                    if preorder:
                        pre.append(x)
                    for y in self.graph[x]:
                        if self.weighted:
                            y, d = y
                        if not seen[y]:
                            stack.append((y, d) if self.weighted else y)
                            if bipartite_graph:
                                bg[y] = (cnt, bg[x][1] ^ 1)
                            if parents or cycle_detection:
                                ps[y] = x
                        elif not finished[y]:
                            if directed_acyclic and dag:
                                dag = False
                                if cycle_detection:
                                    cd = (y, x)
                elif not finished[x]:
                    finished[x] = True
                    if euler_tour:
                        et.append(~x)
                    if postorder or topological_sort:
                        post.append(x)
        if bipartite_graph:
            bg_ = bg
            bg = [[[], []] for i in range(cnt + 1)]
            for tpl in self.edges:
                i, j = tpl[:2] if self.weighted else tpl
                if not bg_[i][1] ^ bg_[j][1]:
                    bg[bg_[i][0]] = False
            for x in range(self.V):
                if bg[bg_[x][0]]:
                    bg[bg_[x][0]][bg_[x][1]].append(x)
        tpl = ()
        if bipartite_graph:
            tpl += (bg, )
        if cycle_detection:
            if dag:
                cd = []
            else:
                y, x = cd
                cd = self.Route_Restoration(y, x, ps)
            tpl += (cd, )
        if directed_acyclic:
            tpl += (dag, )
        if euler_tour:
            tpl += (et, )
        if linked_components:
            tpl += (lc, )
        if parents:
            tpl += (ps, )
        if postorder:
            tpl += (post, )
        if preorder:
            tpl += (pre, )
        if topological_sort:
            if dag:
                tp_sort = post[::-1]
            else:
                tp_sort = []
            tpl += (tp_sort, )
        if len(tpl) == 1:
            tpl = tpl[0]
        return tpl

    def Tree_Diameter(self, weighted=False):
        def Farthest_Point(u):
            dist = self.SS_BFS(
                u, weighted_dist=True) if weighted else self.SS_BFS(
                    u, unweighted_dist=True)
            fp = 0
            for i in range(self.V):
                if dist[fp] < dist[i]:
                    fp = i
            return fp, dist[fp]

        u, d = Farthest_Point(0)
        v, d = Farthest_Point(u)
        return u, v, d

    def SCC(self):
        reverse_graph = [[] for i in range(self.V)]
        for tpl in self.edges:
            i, j = tpl[:2] if self.weighted else tpl
            reverse_graph[j].append(i)
        postorder = self.AP_DFS(postorder=True)
        scc = []
        seen = [False] * self.V
        for s in postorder[::-1]:
            if seen[s]:
                continue
            queue = deque([s])
            seen[s] = True
            lst = []
            while queue:
                x = queue.popleft()
                lst.append(x)
                for y in reverse_graph[x]:
                    if self.weighted:
                        y = y[0]
                    if not seen[y]:
                        seen[y] = True
                        queue.append(y)
            scc.append(lst)
        return scc

    def Build_LCA(self, s):
        self.euler_tour, self.parents, depth = self.SS_DFS(
            s, euler_tour=True, parents=True, unweighted_dist=True)
        self.dfs_in_index = [None] * self.V
        self.dfs_out_index = [None] * self.V
        for i, x in enumerate(self.euler_tour):
            if x >= 0:
                self.dfs_in_index[x] = i
            else:
                self.dfs_out_index[~x] = i
        self.ST = Segment_Tree(2 * self.V, lambda x, y: min(x, y),
                               float('inf'))
        lst = [None] * 2 * self.V
        for i in range(2 * self.V):
            if self.euler_tour[i] >= 0:
                lst[i] = depth[self.euler_tour[i]]
            else:
                lst[i] = depth[self.parents[~self.euler_tour[i]]]
        self.ST.Build(lst)

    def LCA(self, a, b):
        m = min(self.dfs_in_index[a], self.dfs_in_index[b])
        M = max(self.dfs_in_index[a], self.dfs_in_index[b])
        x = self.euler_tour[self.ST.Fold_Index(m, M + 1)]
        if x >= 0:
            return x
        else:
            return self.parents[~x]

    def Dijkstra(self, s, route_restoration=False):
        dist = [float('inf')] * self.V
        dist[s] = 0
        hq = [(0, s)]
        if route_restoration:
            parents = [None] * self.V
            parents[s] = s
        while hq:
            dx, x = heapq.heappop(hq)
            if dist[x] < dx:
                continue
            for y, dy in self.graph[x]:
                if dist[y] > dx + dy:
                    dist[y] = dx + dy
                    if route_restoration:
                        parents[y] = x
                    heapq.heappush(hq, (dist[y], y))
        if route_restoration:
            return dist, parents
        else:
            return dist

    def Bellman_Ford(self, s, route_restoration=False):
        dist = [float('inf')] * self.V
        dist[s] = 0
        if route_restoration:
            parents = [s] * self.V
        for _ in range(self.V - 1):
            for i, j, d in self.edges:
                if dist[j] > dist[i] + d:
                    dist[j] = dist[i] + d
                    if route_restoration:
                        parents[j] = i
                if not self.directed and dist[i] > dist[j] + d:
                    dist[i] = dist[j] + d
                    if route_restoration:
                        parents[i] = j
        negative_cycle = []
        for i, j, d in self.edges:
            if dist[j] > dist[i] + d:
                negative_cycle.append(j)
            if not self.directed and dist[i] > dist[j] + d:
                negative_cycle.append(i)
        if negative_cycle:
            is_negative_cycle = [False] * self.V
            for i in negative_cycle:
                if is_negative_cycle[i]:
                    continue
                else:
                    queue = deque([i])
                    is_negative_cycle[i] = True
                    while queue:
                        x = queue.popleft()
                        for y, d in self.graph[x]:
                            if not is_negative_cycle[y]:
                                queue.append(y)
                                is_negative_cycle[y] = True
                                if route_restoration:
                                    parents[y] = x
            for i in range(self.V):
                if is_negative_cycle[i]:
                    dist[i] = -float('inf')
        if route_restoration:
            return dist, parents
        else:
            return dist

    def Warshall_Floyd(self, route_restoration=False):
        dist = [[float('inf')] * self.V for i in range(self.V)]
        for i in range(self.V):
            dist[i][i] = 0
        if route_restoration:
            parents = [[j for j in range(self.V)] for i in range(self.V)]
        for i, j, d in self.edges:
            if dist[i][j] > d:
                dist[i][j] = d
                if route_restoration:
                    parents[i][j] = i
            if not self.directed and dist[j][i] > d:
                dist[j][i] = d
                if route_restoration:
                    parents[j][i] = j
        for k in range(self.V):
            for i in range(self.V):
                for j in range(self.V):
                    if dist[i][j] > dist[i][k] + dist[k][j]:
                        dist[i][j] = dist[i][k] + dist[k][j]
                        if route_restoration:
                            parents[i][j] = parents[k][j]
        for i in range(self.V):
            if dist[i][i] < 0:
                for j in range(self.V):
                    if dist[i][j] != float('inf'):
                        dist[i][j] = -float('inf')
        if route_restoration:
            return dist, parents
        else:
            return dist

    def Route_Restoration(self, s, g, parents):
        route = [g]
        while s != g and parents[g] != g:
            g = parents[g]
            route.append(g)
        route = route[::-1]
        return route

    def Kruskal(self):
        UF = UnionFind(self.V)
        sorted_edges = sorted(self.edges, key=lambda x: x[2])
        minimum_spnning_tree = []
        for i, j, d in sorted_edges:
            if not UF.Same(i, j):
                UF.Union(i, j)
                minimum_spnning_tree.append((i, j, d))
        return minimum_spnning_tree

    def Ford_Fulkerson(self, s, t):
        max_flow = 0
        residual_graph = [defaultdict(int) for i in range(self.V)]
        if self.weighted:
            for i, j, d in self.edges:
                if not d:
                    continue
                residual_graph[i][j] += d
                if not self.directed:
                    residual_graph[j][i] += d
        else:
            for i, j in self.edges:
                residual_graph[i][j] += 1
                if not self.directed:
                    residual_graph[j][i] += 1
        while True:
            parents = [None] * self.V
            parents[s] = s
            seen = [False] * self.V
            seen[s] = True
            queue = deque([s])
            while queue:
                x = queue.popleft()
                for y in residual_graph[x].keys():
                    if not seen[y]:
                        seen[y] = True
                        queue.append(y)
                        parents[y] = x
                        if y == t:
                            tt = t
                            while tt != s:
                                residual_graph[parents[tt]][tt] -= 1
                                residual_graph[tt][parents[tt]] += 1
                                if not residual_graph[parents[tt]][tt]:
                                    residual_graph[parents[tt]].pop(tt)
                                tt = parents[tt]
                            max_flow += 1
                            break
                else:
                    continue
                break
            else:
                break
        return max_flow

    def BFS(self, s):
        seen = [False] * self.V
        seen[s] = True
        queue = deque([s])

        while queue:
            x = queue.popleft()
            for y in self.graph[x]:
                if self.weighted:
                    y, d = y
                if not seen[y]:
                    seen[y] = True
                    queue.append(y)

        return

    def DFS(self, s):
        seen = [False] * self.V
        finished = [False] * self.V
        stack = [(s, 0)] if self.weighted else [s]

        while stack:
            if self.weighted:
                x, d = stack.pop()
            else:
                x = stack.pop()
            if not seen[x]:
                seen[x] = True
                stack.append((x, d) if self.weighted else x)

                for y in self.graph[x]:
                    if self.weighted:
                        y, d = y
                    if not seen[y]:
                        stack.append((y, d) if self.weighted else y)
            elif not finished[x]:
                finished[x] = True

        return


N, Q = map(int, readline().split())
edges = []
for _ in range(N - 1):
    a, b = map(int, readline().split())
    a -= 1
    b -= 1
    edges.append((a, b))
G = Graph(N, edges=edges)
dist = G.SS_BFS(0, unweighted_dist=True)
for _ in range(Q):
    c, d = map(int, readline().split())
    c -= 1
    d -= 1
    if dist[c] % 2 == dist[d] % 2:
        ans = 'Town'
    else:
        ans = 'Road'
    print(ans)
