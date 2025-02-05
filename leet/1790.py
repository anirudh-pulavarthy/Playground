class Solution:
    def areAlmostEqual(self, s1: str, s2: str) -> bool:
        count = 0 # number of values for which s1[i] != s2[i]

        c1s1, c1s2 = '', ''
        c2s1, c2s2 = '', ''
        for i in range(len(s1)):
            if s1[i] != s2[i]:
                count += 1
                if count > 2: return False
                elif count == 1:  # record chars at i for the first time
                    c1s1, c1s2 = s1[i], s2[i]
                else:   # record chars at i for the second time
                    c2s1, c2s2 = s1[i], s2[i]

        if count == 0: return True
        elif count == 1: return False
        return c1s1 == c2s2 and c1s2 == c2s1