class Solution:
    def queryResults(self, limit: int, queries: List[List[int]]) -> List[int]:
        coloredBalls = defaultdict(int)   # contains color of each ball
        colors = defaultdict(set)   # contains set of balls with color

        ans = []
        for i, color in queries:
            if i in coloredBalls:
                colors[coloredBalls[i]].discard(i)
                if len(colors[coloredBalls[i]]) == 0:
                    del colors[coloredBalls[i]]

            coloredBalls[i] = color
            colors[color].add(i)
            ans.append(len(colors))

        return ans