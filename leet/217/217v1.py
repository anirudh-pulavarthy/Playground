class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        newSet = set(nums)
        return not (len(nums) == len(newSet))