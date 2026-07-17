class Solution:

    VOWELS = set("aeiouAEIOU")

    def count_vowels(self,string : str):

        count = 0
        for char in string:
            if char in self.VOWELS:
                count += 1
        
        return count

    def isvowel(self,ch : char):
        
        return ch in self.VOWELS

    def maxVowels(self, s: str, k: int) -> int:

        vowel = self.count_vowels(s[:k])
        max_vowel = vowel


        for i in range(k,len(s)):
            
            if self.isvowel(s[i-k]):
                vowel -= 1

            if self.isvowel(s[i]):
                vowel += 1

            max_vowel = max(max_vowel,vowel)

        return max_vowel
                




        