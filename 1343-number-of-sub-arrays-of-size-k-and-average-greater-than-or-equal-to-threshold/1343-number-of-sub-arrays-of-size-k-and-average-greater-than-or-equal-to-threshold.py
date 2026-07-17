class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:

        sum_subArray = sum(arr[:k])
        output = 0

        if(sum_subArray/k >= threshold):
            output += 1

        for i in range(k,len(arr)):

            sum_subArray = sum_subArray - arr[i - k] + arr[i]

            if(sum_subArray/k >= threshold):
                output += 1

        return output
        