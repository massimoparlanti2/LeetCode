class Solution:
    def reverse(self, x: int) -> int:
        sign = -1 if x < 0 else 1
        
        # Inverte la stringa del valore assoluto e la riconverte in intero
        res = sign * int(str(abs(x))[::-1])
        
        # Controllo limite 32-bit
        if res < -2**31 or res > 2**31 - 1:
            return 0
            
        return res
