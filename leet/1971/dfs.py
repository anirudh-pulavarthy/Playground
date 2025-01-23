from collections import defaultdict

class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        adjList = defaultdict(list)
        for edge in edges:
            adjList[edge[0]].append(edge[1])
            adjList[edge[1]].append(edge[0])

        def dfs(node, visited):
            if node == destination: return True

            visited.add(node)
            for child in adjList[node]:
                if child not in visited:
                    if dfs(child, visited):
                        return True

            return False

        visited = set()
        return dfs(source, visited)