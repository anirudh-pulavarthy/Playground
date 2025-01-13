class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        ls = len(s)
        lt = len(t)
        i, j = 0, 0
        while i < ls and j < lt:
            if s[i] == t[j]:
                i += 1

            j += 1

        return i == ls