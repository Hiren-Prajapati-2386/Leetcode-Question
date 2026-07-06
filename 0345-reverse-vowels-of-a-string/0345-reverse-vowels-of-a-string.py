class Solution:
    def reverseVowels(self, s: str) -> str:
        s = list(s)
        i = 0
        j = len(s) - 1
        vowels = {'a','e','i','o','u'}

        while(i < j):

            while((s[i].lower() not in vowels) and  i < j):
                i += 1

            while((s[j].lower() not in vowels) and  i < j):
                j -= 1

            temp = s[i]
            s[i] = s[j]
            s[j] = temp

            i += 1
            j -= 1
            
        return "".join(s)
        