class Solution:
    def shiftGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
        m, n = len(grid), len(grid[0])
        total_elements = m * n
        
        
        k = k % total_elements
        
     
        flat_grid = []
        for row in grid:
            flat_grid.extend(row)
            
   
        rotated_flat = flat_grid[-k:] + flat_grid[:-k]
        
        result = []
        for i in range(0, total_elements, n):
            result.append(rotated_flat[i : i + n])
            
        return result
