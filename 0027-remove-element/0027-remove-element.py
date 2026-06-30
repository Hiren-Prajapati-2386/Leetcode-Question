class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        start = 0
        end = len(nums) - 1

        while(start <= end):
            if nums[start] == val:
                if nums[end] != val:
                    temp = nums[start]
                    nums[start] = nums[end]
                    nums[end] = temp
                    start += 1
                    end -= 1

                else:
                    end -= 1
                    temp = nums[start]
                    nums[start] = nums[end]
                    nums[end] = temp
                    start += 1
                    end -= 1

            else:
                start += 1

        return start