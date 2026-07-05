class Solution {
    public int[] pathsWithMaxScore(List<String> board) {
        int n = board.size();
        int MOD = 1_000_000_007;
        int[][] maxScore = new int[n][n];
        int[][] pathCount = new int[n][n];
        
        pathCount[n - 1][n - 1] = 1;
        
        int[][] dirs = {{1, 0}, {0, 1}, {1, 1}};
        
        for (int r = n - 1; r >= 0; r--) {
            for (int c = n - 1; c >= 0; c--) {
                if (board.get(r).charAt(c) == 'X' || pathCount[r][c] == 0) {
                    continue;
                }
                
                int currentScore = maxScore[r][c];
                int currentPaths = pathCount[r][c];
                
                for (int[] dir : dirs) {
                    int nr = r - dir[0];
                    int nc = c - dir[1];
                    
                    if (nr >= 0 && nc >= 0 && board.get(nr).charAt(nc) != 'X') {
                        char nextChar = board.get(nr).charAt(nc);
                        int nextScore = currentScore + (Character.isDigit(nextChar) ? nextChar - '0' : 0);
                        
                        if (nextScore > maxScore[nr][nc]) {
                            maxScore[nr][nc] = nextScore;
                            pathCount[nr][nc] = currentPaths;
                        } else if (nextScore == maxScore[nr][nc]) {
                            pathCount[nr][nc] = (pathCount[nr][nc] + currentPaths) % MOD;
                        }
                    }
                }
            }
        }
        
        return new int[]{maxScore[0][0], pathCount[0][0]};
    }
}
