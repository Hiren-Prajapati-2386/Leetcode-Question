import java.util.*;

class Solution {
    public String smallestPalindrome(String s, int k) {
        int[] count = new int[26];
        for (int i = 0; i < s.length(); i++) {
            count[s.charAt(i) - 'a']++;
        }

        int[] halfCount = new int[26];
        int oddCharIdx = -1;
        int halfLen = 0;

        for (int i = 0; i < 26; i++) {
            if (count[i] % 2 == 1) {
                if (oddCharIdx != -1) return "";
                oddCharIdx = i;
            }
            halfCount[i] = count[i] / 2;
            halfLen += halfCount[i];
        }

        long[][] nCr = new long[halfLen + 1][halfLen + 1];
        for (int i = 0; i <= halfLen; i++) {
            nCr[i][0] = 1;
            for (int j = 1; j <= i; j++) {
                nCr[i][j] = Math.min(1000000000000L, nCr[i - 1][j - 1] + nCr[i - 1][j]);
            }
        }

        long totalPermutations = 1;
        int remainingSlots = halfLen;
        for (int i = 0; i < 26; i++) {
            if (halfCount[i] > 0) {
                totalPermutations = multiplyWithCap(totalPermutations, nCr[remainingSlots][halfCount[i]]);
                remainingSlots -= halfCount[i];
            }
        }

        if (k > totalPermutations) {
            return "";
        }

        StringBuilder leftHalf = new StringBuilder();
        long currentK = k;

        for (int i = 0; i < halfLen; i++) {
            for (int c = 0; c < 26; c++) {
                if (halfCount[c] > 0) {
                    halfCount[c]--;
                    
                    long branchPermutations = 1;
                    int slotsLeft = halfLen - 1 - i;
                    for (int m = 0; m < 26; m++) {
                        if (halfCount[m] > 0) {
                            branchPermutations = multiplyWithCap(branchPermutations, nCr[slotsLeft][halfCount[m]]);
                            slotsLeft -= halfCount[m];
                        }
                    }

                    if (currentK <= branchPermutations) {
                        leftHalf.append((char) ('a' + c));
                        break;
                    } else {
                        currentK -= branchPermutations;
                        halfCount[c]++;
                    }
                }
            }
        }

        StringBuilder fullPalindrome = new StringBuilder(leftHalf);
        if (oddCharIdx != -1) {
            fullPalindrome.append((char) ('a' + oddCharIdx));
        }
        
        for (int i = leftHalf.length() - 1; i >= 0; i--) {
            fullPalindrome.append(leftHalf.charAt(i));
        }

        return fullPalindrome.toString();
    }

    private long multiplyWithCap(long a, long b) {
        if (a == 0 || b == 0) return 0;
        if (a > 1000000000000L / b) return 1000000000000L;
        return a * b;
    }
}
