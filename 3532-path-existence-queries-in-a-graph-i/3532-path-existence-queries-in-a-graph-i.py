class Solution:
    def pathExistenceQueries(self, n: int, nums: List[int], maxDiff: int, queries: List[List[int]]) -> List[bool]:
        
        g = [0] * n
        group_id = 0
        
       
        for i in range(1, n):
            if nums[i] - nums[i - 1] > maxDiff:
                group_id += 1
            g[i] = group_id
            
        #
        return [g[u] == g[v] for u, v in queries]