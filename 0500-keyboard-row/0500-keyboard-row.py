class Solution:
    def findWords(self, words: List[str]) -> List[str]:

        output = []
        

        for word in words:
            lower = word.lower()

            first = 0
            second = 0
            third = 0

            for ch in lower:
                if(ch in "qwertyuiop"):
                    first += 1
                elif(ch in "asdfghjkl"):
                    second += 1
                elif(ch in "zxcvbnm"):
                    third += 1

            if(first == len(lower) or second == len(lower) or third == len(lower)):
                output.append(word)

        return output





        