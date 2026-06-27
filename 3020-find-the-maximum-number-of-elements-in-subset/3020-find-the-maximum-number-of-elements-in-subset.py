class Solution:
    def maximumLength(self, nums: List[int]) -> int:
        
        freq = {}

        for num in nums:
            freq[num] = freq.get(num,0) + 1

        max_length = 1
        

    # we handel all one as an diffrent case .and we select max_length of odd ones
        if 1 in freq:
            one = freq[1]
            if(one % 2 == 0):
                one -= 1

            max_length = max(max_length,one)


        for num in nums:

            if num == 1:
                continue

            curr_num = num
            curr_length = 0

            while(curr_num <= 10**9 and freq.get(int(curr_num),0) >= 2):
                curr_length += 2
                curr_num *= curr_num

            if(curr_num <= 10**9 and freq.get(int(curr_num),0) > 0):
                curr_length += 1

            else:
                curr_length -= 1

            max_length = max(max_length,curr_length)

        return max_length



