class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:

        sorted_arr = sorted(arr)

        rank_map = {}

        rank = 1

        for num in sorted_arr:
            if num not in rank_map:
                rank_map[num] = rank
                rank += 1

        result = [rank_map[x] for x in arr]
        return result