class Solution:
    def numberOfSets(self, n: int, k: int) -> int:
        MOD = 10**9 + 7
        
        # Total items to choose from is (n + k - 1), choosing 2k endpoints
        N = n + k - 1
        R = 2 * k
        
        if N < R:
            return 0
            
        return math.comb(N, R) % MOD