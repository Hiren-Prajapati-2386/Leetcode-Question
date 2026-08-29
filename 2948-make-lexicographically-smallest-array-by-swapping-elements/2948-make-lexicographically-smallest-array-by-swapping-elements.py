from typing import List


class Solution:

  def lexicographicallySmallestArray(self, nums: List[int], limit: int) -> List[int]:
    sorted_pairs = sorted([(val, idx) for idx, val in enumerate(nums)])

    res = [0] * len(nums)
    group_vals = []
    group_indices = []

    for i in range(len(sorted_pairs)):
      val, idx = sorted_pairs[i]


      if group_vals and val - group_vals[-1] > limit:

        group_indices.sort()
        for v, pos in zip(group_vals, group_indices):
          res[pos] = v

        group_vals = []
        group_indices = []


      group_vals.append(val)
      group_indices.append(idx)


    if group_vals:
      group_indices.sort()
      for v, pos in zip(group_vals, group_indices):
        res[pos] = v

    return res