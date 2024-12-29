from typing import List
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        ones = 0
        twos = 0

        for num in nums:
            ones = (ones ^ num) & ~twos
            twos = (twos ^ num) & ~ones

            # print(ones)
            # print(twos)
            # print("=============")
            
        return ones
        