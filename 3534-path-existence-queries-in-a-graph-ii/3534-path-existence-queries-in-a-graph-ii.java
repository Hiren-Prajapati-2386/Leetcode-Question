class Solution {
    public int[] pathExistenceQueries(int n, int[] nums, int maxDiff, int[][] queries) {
        Integer[] idx = new Integer[n];
        for (int i = 0; i < n; i++) {
            idx[i] = i;
        }
        Arrays.sort(idx, (a, b) -> Integer.compare(nums[a], nums[b]));

        int[] pos = new int[n];
        for (int i = 0; i < n; i++) {
            pos[idx[i]] = i;
        }

        int[][] f = new int[n][18];
        int r = 0;
        for (int l = 0; l < n; l++) {
            while (r < n && nums[idx[r]] - nums[idx[l]] <= maxDiff) {
                r++;
            }
            f[l][0] = r - 1;
        }

        for (int k = 1; k < 18; k++) {
            for (int i = 0; i < n; i++) {
                f[i][k] = f[f[i][k - 1]][k - 1];
            }
        }

        int[] ans = new int[queries.length];
        for (int q = 0; q < queries.length; q++) {
            int u = pos[queries[q][0]];
            int v = pos[queries[q][1]];

            if (u == v) {
                ans[q] = 0;
                continue;
            }

            if (u > v) {
                int temp = u;
                u = v;
                v = temp;
            }

            if (f[u][17] < v) {
                ans[q] = -1;
                continue;
            }

            int steps = 0;
            for (int k = 17; k >= 0; k--) {
                if (f[u][k] < v) {
                    u = f[u][k];
                    steps += (1 << k);
                }
            }
            ans[q] = steps + 1;
        }

        return ans;
    }
}
