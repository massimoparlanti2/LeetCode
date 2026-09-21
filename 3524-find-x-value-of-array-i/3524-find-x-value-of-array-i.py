class Solution:
    def resultArray(self, nums: List[int], k: int) -> List[int]:
        result = [0] * k
        # dp[r] memorizza quante sottosequenze che terminano all'elemento precedente 
        # hanno prodotto mod k pari a r.
        dp = {}

        for num in nums:
            val = num % k
            next_dp = {}
            
            # 1. Il sottoinsieme formato solo dall'elemento corrente
            next_dp[val] = next_dp.get(val, 0) + 1
            
            # 2. Estendiamo tutti i resti precedenti con l'elemento corrente
            for r, count in dp.items():
                new_r = (r * val) % k
                next_dp[new_r] = next_dp.get(new_r, 0) + count
            
            # 3. Aggiungiamo i resti trovati in questo passaggio al risultato finale
            for r, count in next_dp.items():
                result[r] += count
                
            dp = next_dp

        return result