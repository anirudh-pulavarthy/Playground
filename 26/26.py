from typing import List

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        count = 1

        p1 = 0
        p2 = 1
        while p2 < len(nums):
            if nums[p2] != nums[p1]:
                p1 = p2
                nums[count] = nums[p2]
                count += 1
            p2 += 1

        print(nums)
        return count

                