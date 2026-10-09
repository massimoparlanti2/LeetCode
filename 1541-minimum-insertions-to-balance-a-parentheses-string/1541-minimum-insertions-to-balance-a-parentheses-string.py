class Solution:
    def minInsertions(self, s: str) -> int:
        ## contare le parentesi + e - e se negativa aggiungere
        insert=0
        right_needed=0

        for i in range(len(s)):
            if s[i]=="(":
                if right_needed%2 !=0:
                    insert+=1
                    right_needed-=1
                right_needed+=2
            else: 
                right_needed-=1
                if right_needed==-1:
                    insert+=1
                    right_needed=1
        
        return insert + right_needed
            