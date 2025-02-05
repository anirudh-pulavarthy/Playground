class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        
        pos, cur, count, total = 0, nums[0], 1, 1

        i = 1
        while i < len(nums):

            if nums[i] == cur:
                count += 1
                if count > 2:
                    pass
                    # print(f"ignore {nums[i]} at {i}")
                else:
                    # print(f"copied {nums[i]} at {i} to {total}")
                    nums[total] = nums[i]
                    total += 1

            else:
                # print(f"found {nums[i]} at {i} & copied to {total}")
                cur = nums[i]
                nums[total] = nums[i]

                count = 1
                total += 1
            
            i += 1

        return total