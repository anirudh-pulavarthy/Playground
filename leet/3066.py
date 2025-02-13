class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        heapify(nums)

        count = 0
        while nums[0] < k:
            x = heappop(nums)
            y = heappop(nums)

            heappush(nums, (min(x, y) * 2 + max(x, y)))
            count += 1

        return count