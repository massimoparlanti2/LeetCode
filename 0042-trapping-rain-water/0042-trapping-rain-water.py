class Solution:
    def trap(self, height: list[int]) -> int:
        n = len(height)
        if n == 0:
            return 0
        
        # 1. Calcolo del massimo a destra per ogni posizione
        rl = [0] * n
        max_right = 0
        for i in range(n - 1, -1, -1):
            max_right = max(max_right, height[i])
            rl[i] = max_right

        # 2. Calcolo del massimo a sinistra e accumulo dell'acqua
        max_left = 0
        water = 0
        for j in range(n):
            max_left = max(max_left, height[j])
            water += min(max_left, rl[j]) - height[j]

        return water