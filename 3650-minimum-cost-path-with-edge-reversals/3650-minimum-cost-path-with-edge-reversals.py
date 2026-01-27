import heapq
from collections import defaultdict
from math import inf

class Solution:
    def minCost(self, n: int, edges):
        adj = defaultdict(list)
        rev = defaultdict(list)

        for u, v, w in edges:
            adj[u].append((v, w))
            rev[v].append((u, w))

        dist = [[inf, inf] for _ in range(n)]
        dist[0][0] = 0

        pq = [(0, 0, 0)]  # cost, node, used

        while pq:
            cost, u, used = heapq.heappop(pq)

            if cost > dist[u][used]:
                continue

            # forward edges (always allowed)
            for v, w in adj[u]:
                if dist[v][used] > cost + w:
                    dist[v][used] = cost + w
                    heapq.heappush(pq, (cost + w, v, used))

            # reversed edges (switches if needed)
            for v, w in rev[u]:
                new_used = 1
                new_cost = cost + 2 * w
                if dist[v][new_used] > new_cost:
                    dist[v][new_used] = new_cost
                    heapq.heappush(pq, (new_cost, v, new_used))

        ans = min(dist[n - 1])
        return ans if ans < inf else -1
