class Solution {
    public int minScore(int n, int[][] roads) {
        List<int[]>[] adj = new ArrayList[n + 1];
        for (int i = 1; i <= n; i++) {
            adj[i] = new ArrayList<>();
        }
        for (int[] road : roads) {
            adj[road[0]].add(new int[]{road[1], road[2]});
            adj[road[1]].add(new int[]{road[0], road[2]});
        }

        int minScore = Integer.MAX_VALUE;
        boolean[] visited = new boolean[n + 1];
        Queue<Integer> queue = new LinkedList<>();
        
        queue.offer(1);
        visited[1] = true;

        while (!queue.isEmpty()) {
            int node = queue.poll();
            for (int[] edge : adj[node]) {
                int neighbor = edge[0];
                int weight = edge[1];
                minScore = Math.min(minScore, weight);
                if (!visited[neighbor]) {
                    visited[neighbor] = true;
                    queue.offer(neighbor);
                }
            }
        }

        return minScore;
    }
}
