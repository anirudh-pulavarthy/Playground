class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        adjList = defaultdict(list)
        for edge in edges:
            adjList[edge[0]].append(edge[1])
            adjList[edge[1]].append(edge[0])

        visited = set()
        queue = deque([source])

        while queue:
            node = queue.popleft()
            if node == destination: return True

            visited.add(node)

            for child in adjList[node]:
                if child not in visited:
                    queue.append(child)
            
        return False