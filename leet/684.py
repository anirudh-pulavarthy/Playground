class Solution:
    def findRedundantConnection(self, edges:List[List[int]]) -> List[int]:
        adList = defaultdict(list)
        for u, v in edges:
            adList[u].append(v)
            adList[v].append(u)
            
        v = edges[0][0] # start bfs from first vertex
        queue = deque([v])
        visited = {v}
        
        while queue:
            v = queue.popleft()
            adj = adList[v]
            for vert in adj:
                
            