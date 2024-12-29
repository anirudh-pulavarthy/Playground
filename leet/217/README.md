# LeetCode Problem 217: Contains Duplicate

## Problem Description
Given an integer array `nums`, return `true` if any value appears at least twice in the array, and return `false` if every element is distinct.

## Example
```python
Input: nums = [1,2,3,1]
Output: true

Input: nums = [1,2,3,4]
Output: false

Input: nums = [1,1,1,3,3,4,3,2,4,2]
Output: true
```

## Constraints
- `1 <= nums.length <= 10^5`
- `-10^9 <= nums[i] <= 10^9`

## Solution
To solve this problem, you can use a set to track the elements you have seen so far. If you encounter an element that is already in the set, return `true`. If you finish iterating through the array without finding any duplicates, return `false`.

## Example Solution in Python
```python
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        seen = set()
        for num in nums:
            if num in seen:
                return true
            seen.add(num)
        return false
```

## Usage
To use this solution, simply call the `containsDuplicate` method with your array of integers.

```python
solution = Solution()
print(solution.containsDuplicate([1, 2, 3, 1]))  # Output: true
print(solution.containsDuplicate([1, 2, 3, 4]))  # Output: false
```