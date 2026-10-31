class Solution {
    public int uniquePaths(int[][] grid) {
        int m = grid.length;
        int n = grid[0].length;
        int MOD = 1_000_000_007;

        int[][][] dest = new int[m][n][2];
        for (int r = m - 1; r >= 0; r--) {
            for (int c = n - 1; c >= 0; c--) {
                if (grid[r][c] == 0) {
                    dest[r][c][0] = r * n + c;
                    dest[r][c][1] = r * n + c;
                } else {
                    dest[r][c][0] = (r + 1 < m) ? dest[r + 1][c][1] : -1;
                    dest[r][c][1] = (c + 1 < n) ? dest[r][c + 1][0] : -1;
                }
            }
        }

        int[][] dp = new int[m][n];
        dp[0][0] = 1;

        for (int r = 0; r < m; r++) {
            for (int c = 0; c < n; c++) {
                if (dp[r][c] == 0) continue;

                if (c + 1 < n) {
                    int target = dest[r][c + 1][0];
                    if (target != -1) {
                        int tr = target / n;
                        int tc = target % n;
                        dp[tr][tc] = (dp[tr][tc] + dp[r][c]) % MOD;
                    }
                }

                if (r + 1 < m) {
                    int target = dest[r + 1][c][1];
                    if (target != -1) {
                        int tr = target / n;
                        int tc = target % n;
                        dp[tr][tc] = (dp[tr][tc] + dp[r][c]) % MOD;
                    }
                }
            }
        }

        return dp[m - 1][n - 1];
    }
}