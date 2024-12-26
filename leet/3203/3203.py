from collections import defaultdict
from heapq import heappush, heappop
from math import ceil
from typing import List

class Solution:
    def minimumDiameterAfterMerge(self, edges1: List[List[int]], edges2: List[List[int]]) -> int:

        def adjacencyList(edges):
            adj = defaultdict(list)
            for v1, v2 in edges:
                adj[v1] = v2
                adj[v2] = v1
            return adj

        def diameter(cur, parent, adj):
            dia = 0
            childPaths = [0, 0]

            for neighbor in adj[cur]:
                if neighbor == parent:
                    continue
                a, b = diameter(neighbor, cur, adj)
                dia = max(dia, a)

                heappush(childPaths, b)
                heappop(childPaths)
                dia = max(dia, sum(childPaths))
            return [dia, 1 + max(childPaths)]

        n, m = len(edges1) + 1, len(edges2) + 1
        adjList1, adjList2 = adjacencyList(edges1), adjacencyList(edges1)
        d1, d2 = diameter(0, -1, edges1), diameter(0, -1, edges2)

        return max(d1, d2, ceil(d1 / 2) + ceil(d2 / 2) + 1)

  