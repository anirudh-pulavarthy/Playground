class Solution:
    def minimumLength(self, s: str) -> int:
        ans = 0
        for ch in {*s}:
            count = s.count(ch)
            ans += 1 if count & 1 else 2
        
        return ans