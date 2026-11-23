# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: ListNode | None, k: int) -> ListNode | None:

        def findKthNode(temp : ListNode,k : int) -> ListNode:

            count = 1
            while temp is not None and count != k:
                temp = temp.next
                count += 1

            return temp

        def reverseLinkList(temp):
            prevNode = None
            point = temp

            while point:
                NextNode = point.next
                point.next = prevNode
                prevNode = point
                point = NextNode

        
        temp = head
        while temp:
            k_node = findKthNode(temp,k)

            if k_node is None:
                if prev:
                    prev.next = temp
                return head

            nextNode = k_node.next
            k_node.next = None

            reverseLinkList(temp)

            if temp == head:
                head = k_node
            else:
                prev.next = k_node
            
            prev = temp
            temp = nextNode

        return head








        