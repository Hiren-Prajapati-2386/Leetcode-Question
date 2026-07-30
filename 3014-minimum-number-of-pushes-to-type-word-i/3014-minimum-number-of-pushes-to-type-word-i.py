class Solution:
    def minimumPushes(self, word: str) -> int:
        
        len_word = len(word)
        output = 0

        if len_word <= 8:
            return len_word

        elif(len_word <= 16):
            return 8 + (len_word-8)*2

        elif(len_word <= 24):
            return 8 + (8*2) + (len_word - 16)*3

        elif(len_word <= 26):
            return 8 + (8*2) + (8*3) + (len_word - 24)*4

        