class Solution:
    def maxNumOfSubstrings(self, s: str) -> list[str]:
        # Step 1: Trova l'indice della prima e dell'ultima occorrenza di ogni carattere
        first = {}
        last = {}
        for i, ch in enumerate(s):
            if ch not in first:
                first[ch] = i
            last[ch] = i
            
        # Step 2: Costruisci tutti gli intervalli validi
        valid_intervals = []
        for ch in set(s):
            left = first[ch]
            right = last[ch]
            
            is_valid = True
            i = left
            while i <= right:
                # Se un carattere interno appare prima di 'left', questo intervallo non può iniziare qui
                if first[s[i]] < left:
                    is_valid = False
                    break
                # Allarga il confine destro per includere tutti i caratteri trovati all'interno
                right = max(right, last[s[i]])
                i += 1
                
            if is_valid:
                valid_intervals.append((left, right))
                
        # Step 3: Ordina gli intervalli in base al punto di fine (Greedy scheduling)
        valid_intervals.sort(key=lambda x: x[1])
        
        # Step 4: Seleziona il maggior numero di sottostringhe non sovrapposte
        results = []
        prev_end = -1
        for left, right in valid_intervals:
            if left > prev_end:
                results.append(s[left:right + 1])
                prev_end = right
                
        return results