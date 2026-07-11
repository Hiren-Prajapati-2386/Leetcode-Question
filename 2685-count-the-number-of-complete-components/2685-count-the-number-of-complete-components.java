import java.util.*;

class Solution {
    public int countCompleteComponents(int n, int[][] edges) {
        List<Integer>[] adj = new ArrayList[n];
        for (int i = 0; i < n; i++) {
            adj[i] = new ArrayList<>();
        }
        
        for (int[] edge : edges) {
            adj[edge[0]].add(edge[1]);
            adj[edge[1]].add(edge[0]);
        }
        
        boolean[] visited = new boolean[n];
        int completeComponentsCount = 0;
        
        for (int i = 0; i < n; i++) {
            if (!visited[i]) {
                int[] stats = new int[2]; 
                dfs(i, adj, visited, stats);
                
                int v = stats[0];
                int totalEdgesCount = stats[1];
                
                if (totalEdgesCount == v * (v - 1)) {
                    completeComponentsCount++;
                }
            }
        }
        
        return completeComponentsCount;
    }
    
    private void dfs(int node, List<Integer>[] adj, boolean[] visited, int[] stats) {
        visited[node] = true;
        stats[0]++; 
        stats[1] += adj[node].size(); 
        
        for (int neighbor : adj[node]) {
            if (!visited[neighbor]) {
                dfs(neighbor, adj, visited, stats);
            }
        }
    }
}
