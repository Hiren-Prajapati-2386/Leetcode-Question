class Solution:


    def addDigits(self, num: int) -> int:

        def findsum(x):
            if(x < 10):
                return x

            sum = 0
            while(x != 0):
                sum +=  x%10
                x = x//10

            return findsum(sum)
        
        return findsum(num)


        