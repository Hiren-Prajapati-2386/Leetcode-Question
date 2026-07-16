class Solution:
    def findWords(self, words: List[str]) -> List[str]:

        row1 = set("qwertyuiop")
        row2 = set("asdfghjkl")
        row3 = set("zxcvbnm")
        
        output = []
        for word in words:
            
            word_set = set(word.lower())
            
            
            if word_set.issubset(row1) or word_set.issubset(row2) or word_set.issubset(row3):
                output.append(word)
                
        return output