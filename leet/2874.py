# Similar to Problem #2140 from April 1
# This problem expects a more efficient solution
# I used Greedy and Prefix computation to get around

class Solution:
    def maximumTripletValue(self, nums: List[int]) -> int:
        size = len(nums)
        prefix_max = [0] * (size)
        suffix_max = [0] * (size)

        for i in range(1, size):
            prefix_max[i] = max(nums[i - 1], prefix_max[i - 1])
            suffix_max[size - 1 - i] = max(nums[size - i], suffix_max[size - i])

        func = lambda a, b, c: (a - b) * c
        ans = 0
        for i in range(1, size - 1):
            ans = max(ans, func(prefix_max[i], nums[i], suffix_max[i]))

        return ans