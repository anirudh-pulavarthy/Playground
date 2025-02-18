# Coin change
# DP practice, Blind 75

class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        coins = sorted(coins)

        dp = [float(inf)] * (amount + 1)
        dp[0] = 0

        for val in range(1, amount + 1):
            for coin in coins:
                if val - coin >= 0:
                    dp[val] = min(dp[val], 1 + dp[val - coin])

        if dp[amount] != float(inf):
            return dp[amount]
        else: return -1

            