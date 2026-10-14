/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode() {}
 *     TreeNode(int val) { this.val = val; }
 *     TreeNode(int val, TreeNode left, TreeNode right) {
 *         this.val = val;
 *         this.left = left;
 *         this.right = right;
 *     }
 * }
 */
class Solution {
    
    public boolean isBalanced(TreeNode root) {
        
        return hightBalanced(root) != -1;

    }

    int hightBalanced(TreeNode root){
        if (root == null) return 0;

        int left = hightBalanced(root.left);
        int right = hightBalanced(root.right);

        if (Math.abs(left - right) > 1){
            return -1;
        }
        if (left == -1 || right == -1){
            return -1;
        }

        return 1 + Math.max(left,right);
    }
}