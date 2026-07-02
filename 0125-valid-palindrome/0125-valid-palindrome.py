class Solution:

    def isalphnumerical(self,char : chr) -> bool:

        if ((48 <= ord(char) <= 57)
            or (65 <= ord(char) <= 90)
            or (97 <= ord(char) <= 122)
            ):
            return True
        return False
    
    def isPalindrome(self,s: str) -> bool:
        
  
        i = 0
        j = len(s)-1
        while(i < j):

            while i < j and not self.isalphnumerical(s[i]):
                i += 1

            
            while i < j and not self.isalphnumerical(s[j]):
                j -= 1

            if(s[i].lower() != s[j].lower()):
                return False
            
            i += 1
            j -= 1
            
        return True