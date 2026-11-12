/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode() {}
 *     ListNode(int val) { this.val = val; }
 *     ListNode(int val, ListNode next) { this.val = val; this.next = next; }
 * }
 */
class Solution {
    public ListNode deleteDuplicates(ListNode head) {

        if (head == null || head.next == null){
            return head;
        }

        ListNode unique = head;
        ListNode point = head.next;

        while (point != null){

            if(unique.val != point.val){
                unique.next = point;
                unique = unique.next;
                point = point.next;
            }
            else{
                point = point.next;
            }
        }

        unique.next = null;
        
        return head;
    }
}