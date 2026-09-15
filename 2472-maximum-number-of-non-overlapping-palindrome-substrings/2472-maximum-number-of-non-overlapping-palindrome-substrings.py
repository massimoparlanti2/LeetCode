class Solution:
    def maxPalindromes(self, s: str, k: int) -> int:
        n = len(s)
        
        # dp[i] = maximum number of non-overlapping palindromes
        # using s[0:i]
        dp = [0] * (n + 1)
        
        for i in range(1, n + 1):
            dp[i] = dp[i - 1]
            
            # Check palindrome of length k
            if i >= k:
                if s[i-k:i] == s[i-k:i][::-1]:
                    dp[i] = max(dp[i], dp[i-k] + 1)
            
            # Check palindrome of length k+1
            if i >= k + 1:
                if s[i-k-1:i] == s[i-k-1:i][::-1]:
                    dp[i] = max(dp[i], dp[i-k-1] + 1)
        
        return dp[n]