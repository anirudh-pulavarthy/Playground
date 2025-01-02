# Daily problem Jan 2
class Solution:
    def vowelStrings(self, words: List[str], queries: List[List[int]]) -> List[int]:
        vowels = set("aeiou")

        pre = []
        count = 0
        pre.append(count)
        for word in words:
            if word[0] in vowels and word[-1] in vowels:
                count += 1
            pre.append(count)

        ans = []
        for q in queries:
            l, r = q
            ans.append(pre[r + 1] - pre[l])

        return ans