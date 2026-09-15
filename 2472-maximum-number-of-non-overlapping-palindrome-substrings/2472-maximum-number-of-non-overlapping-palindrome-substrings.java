class Solution {
    public int maxPalindromes(String s, int k) {
        int n = s.length();
        int count = 0;
        int lastEnd = -1;

        for (int center = 0; center < 2 * n - 1; center++) {
            int l = center / 2;
            int r = l + (center % 2);

            while (l >= 0 && r < n && s.charAt(l) == s.charAt(r)) {
                if (r - l + 1 >= k) {
                    if (l > lastEnd) {
                        count++;
                        lastEnd = r;
                        break;
                    }
                }
                l--;
                r++;
            }
        }

        return count;
    }
}