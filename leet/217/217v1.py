class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        newSet = set(nums)
        if(len(nums) == len(newSet)):
            return False
        else:
            return True