class Solution:
    def findThePrefixCommonArray(self, A: List[int], B: List[int]) -> List[int]:
        def countTwos(fre):
            c = 0
            for key, val in fre.items():
                if val == 2: c += 1
            return c

        ans = []

        freq = defaultdict(int)
        for i in range(len(A)):
            freq[A[i]] += 1
            freq[B[i]] += 1

            ans.append(countTwos(freq))

        return ans