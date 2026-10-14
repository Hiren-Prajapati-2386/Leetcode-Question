class Solution {
    public String maxSumOfSquares(int num, int sum) {
        if (sum < 1 || sum > 9L * num) {
            return "";
        }

        StringBuilder sb = new StringBuilder(num);
        int remainingSum = sum;
        int remainingDigits = num;

        while (remainingDigits > 0) {
            if (remainingSum >= 9) {
                sb.append('9');
                remainingSum -= 9;
            } else if (remainingSum > 0) {
                sb.append(remainingSum);
                remainingSum = 0;
            } else {
                sb.append('0');
            }
            remainingDigits--;
        }

        return sb.toString();
    }
}