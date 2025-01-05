from typing import List
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        ans = []

        current = []
        def dfs(i):
            if i >= len(nums):
                ans.append(current[:])
                return
            
            # if 'i'th element isn't in the subset
            dfs(i + 1)

            # if 'i'th element is in the subset
            current.append(nums[i])
            dfs(i + 1)
            current.pop()

        dfs(0)
        return ans
    
if __name__ == "__main__":
    ob = Solution()
    print(ob.subsets([1, 2, 3]))

    
# class Solution:
#     def subsets(self, nums: List[int]) -> List[List[int]]:
#         length = len(nums)

#         def kthBitSet(n, k) -> bool:
#             return n & (1 << (k))

#         def unsetKthBit(n, k):
#             return n & ~(1 << (k))

#         ans = []
#         for i in range(length):
#             print(f"Processing {i} now")
#             curSet = []
#             # check what bits are set
#             # based on what bits are set, add those elements in nums at
#             # those indices to the ans set
#             index = 0
#             while i and (index < length):
#                 if kthBitSet(i, index):
#                     print(f"{index}th bit is set in {i}")
#                     v = nums[index]
#                     curSet.append(v)
#                     i = unsetKthBit(i, index)
                
#                 index += 1
#             ans.append(curSet)

#         return ans
