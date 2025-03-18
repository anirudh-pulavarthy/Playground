class Solution:
    def longestNiceSubarray(self, nums: List[int]) -> int:
        maxLen = 1

        l, r = 0, 0
        # setBits = nums[l]
        while r < len(nums):
            # print(l, r)
            if l == r:
                setBits = nums[l]
                r += 1
            elif setBits & nums[r] == 0:
                # print(f"setBits is {setBits} for {nums[l]} and {nums[r]}")
                setBits = setBits | nums[r]
                maxLen = max(maxLen, r - l + 1)
                # print(f"Maxlen is {maxLen} for {l} and {r}")
                r += 1
            else:
                setBits = setBits & (~nums[l])
                l += 1
            
        return maxLen