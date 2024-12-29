# LeetCode Problem 137: Single Number II

## Problem Description
Given an integer array `nums` where every element appears three times except for one, which appears exactly once. Find the single element and return it.

You must implement a solution with a linear runtime complexity and use only constant extra space.

## Example
**Example 1:**
```
Input: nums = [2,2,3,2]
Output: 3
```

**Example 2:**
```
Input: nums = [0,1,0,1,0,1,99]
Output: 99
```

## Constraints
- `1 <= nums.length <= 3 * 10^4`
- `-2^31 <= nums[i] <= 2^31 - 1`
- Each element in `nums` appears exactly three times except for one element which appears once.

## Solution Approach
To solve this problem, you can use bitwise operations to count the number of 1s at each bit position across all numbers. Since every number except one appears three times, the sum of bits at each position will be a multiple of three for those numbers. The bits of the single number can be found by taking the modulo 3 of the sum of bits at each position.

## Code Example
Here is a Python implementation of the solution:

```python
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        ones, twos = 0, 0
        for num in nums:
            ones = (ones ^ num) & ~twos
            twos = (twos ^ num) & ~ones
        return ones
```

This code uses two variables `ones` and `twos` to keep track of the bits that have appeared once and twice respectively. The final result is the number appearing only once and is left in the variable `ones`.
