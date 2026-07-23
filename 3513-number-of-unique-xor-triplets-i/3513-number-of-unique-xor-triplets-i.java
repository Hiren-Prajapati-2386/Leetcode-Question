class Solution {
    public int uniqueXorTriplets(int[] nums) {
        int n = nums.length;
        if (n < 3) {
            return n;
        }
        int highestBit = 31 - Integer.numberOfLeadingZeros(n);
        return 1 << (highestBit + 1);
    }
}
