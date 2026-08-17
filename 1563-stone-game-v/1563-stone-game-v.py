class Solution:
    def stoneGameV(self, stoneValue: List[int]) -> int:
        n = len(stoneValue)
        pref = [0] * (n + 1)
        for i in range(n):
            pref[i + 1] = pref[i] + stoneValue[i]
            
        dp = [[0] * n for _ in range(n)]
        max_left = [[0] * n for _ in range(n)]
        max_right = [[0] * n for _ in range(n)]
        
        for i in range(n):
            dp[i][i] = 0
            max_left[i][i] = stoneValue[i]
            max_right[i][i] = stoneValue[i]
            
        mids = [i for i in range(n)]
        
        for length in range(2, n + 1):
            for i in range(n - length + 1):
                j = i + length - 1
          
                while mids[i] < j - 1 and (pref[mids[i] + 1] - pref[i]) < (pref[j + 1] - pref[mids[i] + 1]):
                    mids[i] += 1
                    
                mid = mids[i]
                left_sum = pref[mid + 1] - pref[i]
                right_sum = pref[j + 1] - pref[mid + 1]
                
                res = 0
                
                
                if left_sum < right_sum:
                    res = max_left[i][mid]
          
                else:
                
                    if mid > i:
                        res = max(res, max_left[i][mid - 1])
              
                    if mid + 1 <= j:
                        res = max(res, max_right[mid + 1][j])
                     
                    if left_sum == right_sum:
                        res = max(res, max_left[i][mid])

                dp[i][j] = res
                
                current_total = pref[j + 1] - pref[i]
                max_left[i][j] = max(max_left[i][j - 1], res + current_total)
                max_right[i][j] = max(max_right[i + 1][j], res + current_total)
                
        return dp[0][n - 1]
