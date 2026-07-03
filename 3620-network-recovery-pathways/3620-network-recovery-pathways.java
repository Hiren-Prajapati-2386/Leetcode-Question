import java.util.*;

class Solution {
    public int findMaxPathScore(int[][] edges, boolean[] online, long k) {
        int n = online.length;
        List<int[]>[] graph = new ArrayList[n];
        for (int i = 0; i < n; i++) {
            graph[i] = new ArrayList<>();
        }
        
        TreeSet<Integer> uniqueCosts = new TreeSet<>();
        for (int[] edge : edges) {
            int u = edge[0];
            int v = edge[1];
            int cost = edge[2];
            if (online[u] && online[v]) {
                graph[u].add(new int[]{v, cost});
                uniqueCosts.add(cost);
            }
        }
        
        if (uniqueCosts.isEmpty()) {
            return -1;
        }
        
        List<Integer> costList = new ArrayList<>(uniqueCosts);
        int low = 0;
        int high = costList.size() - 1;
        int ans = -1;
        
        while (low <= high) {
            int mid = low + (high - low) / 2;
            int threshold = costList.get(mid);
            
            if (isValid(graph, n, threshold, k)) {
                ans = threshold;
                low = mid + 1;
            } else {
                high = mid - 1;
            }
        }
        
        return ans;
    }
    
    private boolean isValid(List<int[]>[] graph, int n, int threshold, long maxCost) {
        long[] minCostToNode = new long[n];
        Arrays.fill(minCostToNode, Long.MAX_VALUE);
        minCostToNode[0] = 0;
        
        int[] inDegree = new int[n];
        for (int u = 0; u < n; u++) {
            for (int[] edge : graph[u]) {
                if (edge[1] >= threshold) {
                    inDegree[edge[0]]++;
                }
            }
        }
        
        Queue<Integer> queue = new LinkedList<>();
        for (int i = 0; i < n; i++) {
            if (inDegree[i] == 0) {
                queue.add(i);
            }
        }
        
        while (!queue.isEmpty()) {
            int u = queue.poll();
            long currentCost = minCostToNode[u];
            
            for (int[] edge : graph[u]) {
                int v = edge[0];
                int weight = edge[1];
                
                if (weight >= threshold) {
                    if (currentCost != Long.MAX_VALUE && currentCost + weight < minCostToNode[v]) {
                        minCostToNode[v] = currentCost + weight;
                    }
                    inDegree[v]--;
                    if (inDegree[v] == 0) {
                        queue.add(v);
                    }
                }
            }
        }
        
        return minCostToNode[n - 1] <= maxCost;
    }
}
