class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        caratteri = set()
        left = 0
        max_len = 0

        for right in range(len(s)):
            # Se il carattere è già nella finestra, rimuoviamo i caratteri da sinistra
            # finché non rimuoviamo il duplicato
            while s[right] in caratteri:
                caratteri.remove(s[left])
                left += 1

            # Aggiungiamo il nuovo carattere e aggiorniamo la lunghezza massima
            caratteri.add(s[right])
            max_len = max(max_len, right - left + 1)

        return max_len