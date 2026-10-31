class Solution {
    public int minOperations(String s) {
        int n = s.length();
        if (n <= 1) return 0;

        // Check if already sorted
        boolean sorted = true;
        for (int i = 1; i < n; i++) {
            if (s.charAt(i) < s.charAt(i - 1)) {
                sorted = false;
                break;
            }
        }
        if (sorted) return 0;

        // Impossible case
        if (n == 2) return -1;

        // Find global minimum and maximum characters
        char minChar = 'z';
        char maxChar = 'a';
        for (int i = 0; i < n; i++) {
            char c = s.charAt(i);
            if (c < minChar) minChar = c;
            if (c > maxChar) maxChar = c;
        }

        // 1 operation:
        // - Smallest char is already in the first position (sort s[1...n-1])
        // - Largest char is already in the last position (sort s[0...n-2])
        if (s.charAt(0) == minChar || s.charAt(n - 1) == maxChar) {
            return 1;
        }

        // 3 operations:
        // The unique maximum is at index 0 AND the unique minimum is at index n-1.
        // Check if minChar appears anywhere in s[0...n-2]
        boolean minInPrefix = false;
        for (int i = 0; i < n - 1; i++) {
            if (s.charAt(i) == minChar) {
                minInPrefix = true;
                break;
            }
        }

        // Check if maxChar appears anywhere in s[1...n-1]
        boolean maxInSuffix = false;
        for (int i = 1; i < n; i++) {
            if (s.charAt(i) == maxChar) {
                maxInSuffix = true;
                break;
            }
        }

        if (!minInPrefix && !maxInSuffix) {
            return 3;
        }

        // Otherwise, 2 operations are always sufficient
        return 2;
    }
}