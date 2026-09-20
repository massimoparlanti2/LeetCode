class Solution:
    def reverseDegree(self, s: str) -> int:
        total = 0
        for i, char in enumerate(s, start=1):
            # Valore dell'alfabeto invertito: 'a' -> 26, 'b' -> 25, ..., 'z' -> 1
            rev_alphabet_value = 26 - (ord(char) - ord('a'))
            
            # Somma il prodotto con la posizione 1-indexed (i)
            total += rev_alphabet_value * i
            
        return total