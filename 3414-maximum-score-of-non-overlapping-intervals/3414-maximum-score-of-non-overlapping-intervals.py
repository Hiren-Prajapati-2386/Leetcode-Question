from bisect import bisect_right
from typing import List


class Solution:

    def maximumWeight(self, intervals: List[List[int]]) -> List[int]:
        n = len(intervals)

        # intervals with original indices: (l, r, weight, original_index)
        events = sorted(
            (l, r, w, i) for i, (l, r, w) in enumerate(intervals)
        )  # sort by l
        # Sort by right endpoint to enable binary search on non-overlapping intervals
        events.sort(key=lambda x: x[1])

        rights = [ev[1] for ev in events]

        # dp[k][i] = (weight, tuple_of_original_indices)
        # k ranges from 0 to 4
        dp = [[(0, ())] * (n + 1) for _ in range(5)]

        def compare(cand1, cand2):
            """Returns the better choice: larger weight, then lexicographically smaller indices."""
            w1, idx1 = cand1
            w2, idx2 = cand2
            if w1 > w2:
                return cand1
            if w2 > w1:
                return cand2
            return cand1 if idx1 < idx2 else cand2

        for i in range(1, n + 1):
            l, r, w, orig_idx = events[i - 1]

            # Find the largest j such that events[j-1].r < l
            # Since intervals touching boundaries are overlapping, we strictly need r < l
            prev_j = bisect_right(rights, l - 1)

            for k in range(1, 5):
                # Option 1: Do not take intervals[i - 1]
                best = dp[k][i - 1]

                # Option 2: Take intervals[i - 1]
                prev_w, prev_indices = dp[k - 1][prev_j]
                new_w = prev_w + w
                # Maintain sorted order of indices
                new_indices = tuple(sorted(prev_indices + (orig_idx,)))

                cand = (new_w, new_indices)
                dp[k][i] = compare(best, cand)

 
        ans_state = (0, ())
        for k in range(1, 5):
            ans_state = compare(ans_state, dp[k][n])

        return list(ans_state[1])