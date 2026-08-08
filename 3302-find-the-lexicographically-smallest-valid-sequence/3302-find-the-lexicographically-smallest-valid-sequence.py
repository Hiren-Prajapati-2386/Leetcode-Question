from typing import List
from bisect import bisect_left

class Solution:
    def validSequence(self, word1: str, word2: str) -> List[int]:
        n, m = len(word1), len(word2)

        pos = [[] for _ in range(26)]
        for i, c in enumerate(word1):
            pos[ord(c) - 97].append(i)

        def prev_pos(c, limit):
            arr = pos[ord(c) - 97]
            k = bisect_left(arr, limit)
            return arr[k - 1] if k else -1

        exact = [-1] * (m + 1)
        exact[m] = n

        limit = n
        for j in range(m - 1, -1, -1):
            exact[j] = prev_pos(word2[j], limit)
            limit = exact[j]

        one = [-1] * (m + 1)
        one[m] = n

        for j in range(m - 1, -1, -1):
            same = prev_pos(word2[j], one[j + 1])

            limit = exact[j + 1]
            diff = -1

            if limit > 0:
                i = limit - 1
                if word1[i] != word2[j]:
                    diff = i
                else:
                    diff = prev_pos(word2[j], i)

            one[j] = max(same, diff)

        ans = []
        prev = -1
        changed = False

        for j in range(m):
            i = prev + 1

            while i < n:
                if changed:
                    ok = (
                        word1[i] == word2[j]
                        and (j == m - 1 or i < exact[j + 1])
                    )
                else:
                    if word1[i] == word2[j]:
                        ok = j == m - 1 or i < one[j + 1]
                    else:
                        ok = j == m - 1 or i < exact[j + 1]

                if ok:
                    ans.append(i)
                    if word1[i] != word2[j]:
                        changed = True
                    prev = i
                    break

                i += 1
            else:
                return []

        return ans