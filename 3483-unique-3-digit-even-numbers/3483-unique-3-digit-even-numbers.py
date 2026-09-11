class Solution:
    def totalNumbers(self, digits: List[int]) -> int:

        digit_counts = Counter(digits)
        count = 0

        # Every 3-digit even number is in the range [100, 998] with step 2
        for num in range(100, 1000, 2):
            d1 = num // 100
            d2 = (num // 10) % 10
            d3 = num % 10

            needed = Counter([d1, d2, d3])

            # Check if available digits satisfy the required counts
            if all(digit_counts[d] >= needed[d] for d in needed):
                count += 1

        return count
            