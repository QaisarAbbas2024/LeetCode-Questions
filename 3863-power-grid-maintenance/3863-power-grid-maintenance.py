from typing import List
import heapq

class Solution:
    def processQueries(self, c: int, connections: List[List[int]], queries: List[List[int]]) -> List[int]:
        # convert to 0-based
        n = c
        for i in range(len(connections)):
            connections[i][0] -= 1
            connections[i][1] -= 1

        # build adjacency
        adj = [[] for _ in range(n)]
        for u, v in connections:
            adj[u].append(v)
            adj[v].append(u)

        # compute static components (iterative DFS)
        comp_id = [-1] * n
        comp_cnt = 0
        for i in range(n):
            if comp_id[i] != -1:
                continue
            stack = [i]
            comp_id[i] = comp_cnt
            while stack:
                u = stack.pop()
                for w in adj[u]:
                    if comp_id[w] == -1:
                        comp_id[w] = comp_cnt
                        stack.append(w)
            comp_cnt += 1

        # Prepare ops and determine which close operations were effective by simulating forward
        ops = []
        effective_close = []   # same length as ops; True if this close actually changed state
        active = [True] * n    # simulate forward
        for t, x in queries:
            x -= 1
            ops.append((t, x))
            if t == 2:
                if active[x]:
                    effective_close.append(True)
                    active[x] = False
                else:
                    effective_close.append(False)
            else:
                effective_close.append(None)

        # now 'active' contains final state after all forward ops
        # build min-heaps for each static component using currently active nodes
        heaps = [[] for _ in range(comp_cnt)]
        for i in range(n):
            if active[i]:
                heapq.heappush(heaps[comp_id[i]], i)

        # process queries in reverse: only undo effective closes
        ans_rev = []
        # iterate reversed with index to check effective_close
        for idx in range(len(ops)-1, -1, -1):
            t, x = ops[idx]
            eff = effective_close[idx]
            if t == 1:  # ask
                if active[x]:
                    ans_rev.append(x)
                else:
                    comp = comp_id[x]
                    if not heaps[comp]:
                        ans_rev.append(-1)
                    else:
                        ans_rev.append(heaps[comp][0])
            else:  # t == 2, reverse = reopen but only if this close was effective
                if eff:
                    # this close had turned an online node to offline in forward,
                    # so undoing it now re-activates the node
                    if not active[x]:
                        active[x] = True
                        heapq.heappush(heaps[comp_id[x]], x)
                # if eff is False -> this close did nothing forward; undoing does nothing

        # reverse answers and convert to 1-based
        ans = []
        for v in reversed(ans_rev):
            ans.append(v + 1 if v != -1 else -1)
        return ans
