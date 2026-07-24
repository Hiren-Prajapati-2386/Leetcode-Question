from typing import List

class Solution:
    def uniqueXorTriplets(self, nums: List[int]) -> int:
  
        unique_nums = list(set(nums))
        
     
        pairs = set()
        for x in unique_nums:
            for y in unique_nums:
                pairs.add(x ^ y)
        
       
        triplets = set()
        for p in pairs:
            for z in unique_nums:
                triplets.add(p ^ z)
  

        return len(triplets)
