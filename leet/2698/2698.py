# Using a recursive strategy
class Solution:
    def punishmentNumber(self, n: int) -> int:

        def partition(position: int, cur: int, string: str, target: int) -> bool:
            if position == len(string): #if end of the string is reached, check target
                return cur == target

            for j in range(position, len(string)):
                if partition(j + 1, cur + int(string[position : j + 1]), string, target):
                    return True

            return False

        ans = 0
        for i in range(1, n + 1):
            if partition(0, 0, str(i * i), i):
                ans += (i * i)

        return ans
