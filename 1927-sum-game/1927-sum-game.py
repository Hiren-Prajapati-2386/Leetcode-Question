class Solution:
    def sumGame(self, num: str) -> bool:
        n = len(num)
        half = n // 2
        
        sum1, q1 = 0, 0
        for i in range(half):
            if num[i] == '?':
                q1 += 1
            else:
                sum1 += int(num[i])
                
        sum2, q2 = 0, 0
        for i in range(half, n):
            if num[i] == '?':
                q2 += 1
            else:
                sum2 += int(num[i])
                
        return (sum1 - sum2) * 2 != (q2 - q1) * 9
