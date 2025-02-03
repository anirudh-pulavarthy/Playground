class Solution:
    def longestMonotonicSubarray(self, nums: List[int]) -> int:
        longest = 1

        # check for longest strictly increasing subsequence
        i, j, size = 0, 1, len(nums)
        while j < size:
            if nums[j] > nums[j - 1]:
                longest = max(longest, j - i + 1)
            else:
                i = j

            j += 1

        # check for longest strictly decreasing subsequence
        i, j = 0, 1
        while j < size:
            if nums[j] < nums[j - 1]:
                longest = max(longest, j - i + 1)
            else:
                i = j

            j += 1

        return longest