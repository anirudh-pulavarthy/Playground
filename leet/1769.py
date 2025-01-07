# Min # of operations to move all balls
# Brute Force approach would be to sum abs(i - j) for each j where
# boxes[j] == '1'. This would take O(n^2) time

# Could use a precomputed sum of indices to compute ans[i] in 2 passes
# Resulting solution would take O(n)

from typing import List

class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        countL, sumL = 0, 0
        countR, sumR = 0, 0

        for i, s in enumerate(boxes):
            if s == '1':
                sumR += (i + 1)
                countR += 1

        ans = []
        for i, s in enumerate(boxes):
            if s == '1':
                sumL += countL
                countL += 1
                sumR -= countR
                countR -= 1
            else:
                sumL += countL
                sumR -= countR
            ans.append(sumL + sumR)
            
        return ans
