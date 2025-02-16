# Better solution if n is less than 1000
class Solution:
    def punishmentNumber(self, n: int) -> int:

        def partition(num: int, target: int) -> bool:
            # print(f"Called partition {num}, {target}")
            if target < 0 or num < target: return False
            elif num == target:
                return True

            return partition(num // 10, target - (num % 10) ) \
                or partition(num // 100, target - (num % 100) ) \
                or partition(num // 1000, target - (num % 1000) )


        ans = 0
        for i in range(1, n + 1):
            if partition(i * i, i):
                ans += (i * i)

        return ans
