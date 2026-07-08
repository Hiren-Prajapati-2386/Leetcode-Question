import java.util.*;

class Solution {
    public int[] sumAndMultiply(String s, int[][] queries) {
        int m = s.length();
        int MOD = 1000000007;

        int[] cntN0 = new int[m + 1];
        int[] sumD = new int[m + 1];
        long[] p = new long[m + 1];
        long[] POW10 = new long[m + 1];

        POW10[0] = 1;
        for (int i = 1; i <= m; i++) {
            POW10[i] = (POW10[i - 1] * 10) % MOD;
        }

        for (int i = 0; i < m; i++) {
            int d = s.charAt(i) - '0';
            if (d != 0) {
                cntN0[i + 1] = cntN0[i] + 1;
                sumD[i + 1] = sumD[i] + d;
                p[i + 1] = (p[i] * 10 + d) % MOD;
            } else {
                cntN0[i + 1] = cntN0[i];
                sumD[i + 1] = sumD[i];
                p[i + 1] = p[i];
            }
        }

        int[] ans = new int[queries.length];
        for (int i = 0; i < queries.length; i++) {
            int l = queries[i][0];
            int r = queries[i][1];

            int n0 = cntN0[r + 1] - cntN0[l];
            int sd = sumD[r + 1] - sumD[l];

            long x = (p[r + 1] - p[l] * POW10[n0] % MOD + MOD) % MOD;
            ans[i] = (int) (x * sd % MOD);
        }

        return ans;
    }
}
