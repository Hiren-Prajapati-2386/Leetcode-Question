class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:

        count = [0,0,0,0,0]
        for i in range(0,len(text)):
            if(text[i] == 'b'):
                count[0] = count[0] + 1  #b
            if(text[i] == 'a'):
                count[1] = count[1] + 1  #a
            if(text[i] == 'l'):
                count[2] = count[2] + 1  #l
            if(text[i] == 'o'):
                count[3] = count[3] + 1  #0
            if(text[i] == 'n'):
                count[4] = count[4] + 1  #p
        
        return min(count[0], count[1], count[2] // 2, count[3] // 2, count[4])