# Palindrome number

class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0: return False
        elif x // 10 == 0: return True

        reverse = 0
        org = x
        while org != 0:
            reverse *= 10
            reverse += (org % 10)
            org = org // 10
        
        return reverse == x
        
if __name__ == "__main__":

    s = Solution()
    res = s.isPalindrome(313)
    print("Solution = ", res)