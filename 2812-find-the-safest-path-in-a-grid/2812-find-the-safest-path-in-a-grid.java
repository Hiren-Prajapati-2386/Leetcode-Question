import java.util.*;

class Solution {
    public int maximumSafenessFactor(List<List<Integer>> grid) {
        int n = grid.size();
        
        if (grid.get(0).get(0) == 1 || grid.get(n - 1).get(n - 1) == 1) {
            return 0;
        }

        int[][] thiefDist = new int[n][n];
        for (int[] row : thiefDist) {
            Arrays.fill(row, -1);
        }

        Queue<int[]> queue = new LinkedList<>();

     
        for (int r = 0; r < n; r++) {
            for (int c = 0; c < n; c++) {
                if (grid.get(r).get(c) == 1) {
                    queue.offer(new int[]{r, c});
                    thiefDist[r][c] = 0;
                }
            }
        }

        int[][] dirs = {{0, 1}, {0, -1}, {1, 0}, {-1, 0}};

        while (!queue.isEmpty()) {
            int[] cell = queue.poll();
            int r = cell[0];
            int c = cell[1];

            for (int[] d : dirs) {
                int nr = r + d[0];
                int nc = c + d[1];

                if (nr >= 0 && nr < n && nc >= 0 && nc < n && thiefDist[nr][nc] == -1) {
                    thiefDist[nr][nc] = thiefDist[r][c] + 1;
                    queue.offer(new int[]{nr, nc});
                }
            }
        }


        PriorityQueue<int[]> maxHeap = new PriorityQueue<>((a, b) -> b[0] - a[0]);
        boolean[][] visited = new boolean[n][n];

        maxHeap.offer(new int[]{thiefDist[0][0], 0, 0});
        visited[0][0] = true;

        while (!maxHeap.isEmpty()) {
            int[] curr = maxHeap.poll();
            int safeness = curr[0];
            int r = curr[1];
            int c = curr[2];

            if (r == n - 1 && c == n - 1) {
                return safeness;
            }

            for (int[] d : dirs) {
                int nr = r + d[0];
                int nc = c + d[1];

                if (nr >= 0 && nr < n && nc >= 0 && nc < n && !visited[nr][nc]) {
                    visited[nr][nc] = true;
                    int nextSafeness = Math.min(safeness, thiefDist[nr][nc]);
                    maxHeap.offer(new int[]{nextSafeness, nr, nc});
                }
            }
        }

        return 0;
    }
}
