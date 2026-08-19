class Solution:
    def maxNumberOfFamilies(self, n: int, reservedSeats: List[List[int]]) -> int:
        reserved_rows = defaultdict(int)
        
        for row, seat in reservedSeats:
            if 2 <= seat <= 9:
                reserved_rows[row] |= (1 << (seat - 2))
                
        left_mask = 0b00001111    # Seats 2,3,4,5
        middle_mask = 0b00111100  # Seats 4,5,6,7
        right_mask = 0b11110000   # Seats 6,7,8,9
        
        ans = (n - len(reserved_rows)) * 2
        
        for mask in reserved_rows.values():
            left_free = (mask & left_mask) == 0
            right_free = (mask & right_mask) == 0
            middle_free = (mask & middle_mask) == 0
            
            if left_free and right_free:
                ans += 2
            elif left_free or right_free or middle_free:
                ans += 1
                
        return ans
