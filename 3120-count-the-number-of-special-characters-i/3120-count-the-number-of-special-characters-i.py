class Solution:
    def numberOfSpecialChars(self, word: str) -> int:
        v = []
        for i in word:
            if i not in v:
                v.append(i)
        
        count = 0
        for char in v:
            if char.islower() and char.upper() in v:
                count += 1
                
        return count
