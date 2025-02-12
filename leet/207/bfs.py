class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:

        if len(prerequisites) == 0: return True

        ad = defaultdict(list)  # the adjacency list of the graph
        for i, j in prerequisites:
            if i == j: return False # a course cannot have itself as a prereq!!!
            ad[i].append(j)

        visited = set()
        queue = deque()
        queue.append(prerequisites[0][0])

        while queue:
            node = queue.popleft()

            if node in visited:
                return False    # there's a cycle!!

            visited.add(node)
            queue.discard(node)
            
            queue.extend(ad[node])

        return True