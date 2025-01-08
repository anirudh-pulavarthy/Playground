# Uses Moore's voting algorithm
# O(n) time and O(1) aux space
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count, candidate = 0, None
        for i in nums:
            if count == 0:
                candidate = i
                count += 1
            elif candidate == i:
                count += 1
            else:
                count -= 1

        return candidate