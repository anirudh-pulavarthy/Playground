# Problem 1: Two Sum
from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        nums_dict = {}
        for i, num in enumerate(nums):
            if num in nums_dict:
                nums_dict[num].append(i)
            else:
                nums_dict[num] = [i]
        
        for i, num in enumerate(nums):
            find = target - num

            if find in nums_dict:
                val = nums_dict[find]

                if find == num and len(val) > 1:
                    return val
                elif find != num:
                    return [i, val[0]]

if __name__ == "__main__":
    arr = [3, 2, 4]

    s = Solution()
    ans = s.twoSum(arr, 6)
    print(ans)