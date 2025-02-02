class Solution:
    def check(self, nums: List[int]) -> bool:
        if len(nums) <= 2: return True

        i = 1
        ok = True
        numsLen = len(nums)
        while ok and i < numsLen:
            if nums[i - 1] <= nums[i]:
                i += 1
            else:
                ok = False

        if ok: return True

        #assert nums[i] <= nums[0]
        if nums[i] > nums[0]: return False

        i += 1
        while i < numsLen:
            if not nums[i - 1] <= nums[i]:
                return False
            i += 1

        if nums[i - 1] > nums[0]: return False
        return True
