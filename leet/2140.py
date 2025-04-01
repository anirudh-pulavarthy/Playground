class Solution:
    def mostPoints(self, questions: List[List[int]]) -> int:
        dp = [0] * len(questions)

        for i in reversed(range(len(questions))):
            ans_exclude = dp[i + 1] if (i + 1) < len(dp) else 0

            next_solvable_idx = i + questions[i][1] + 1    # points to (i + brainpower(i) + 1)
            next_ans = dp[next_solvable_idx] if next_solvable_idx < len(dp) else 0
            ans_include = questions[i][0] + next_ans
            dp[i] = max(ans_exclude, ans_include)

        # return max(dp)
        return dp[0]    # dp[0] should hold the maximum possible points one can earn
