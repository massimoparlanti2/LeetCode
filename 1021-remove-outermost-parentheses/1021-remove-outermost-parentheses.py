class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        count=0
        count_prec=0
        stringa=""
        for i in range(len(s)):
            count_prec=count
            if s[i] == "(":
                count+=1
            if s[i]==")":
                count-=1
            if count_prec>1 or count>1:
                stringa+=s[i]
        return stringa