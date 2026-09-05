# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:

        pointer = head
        counter = 0

        while(pointer is not None):
            counter += 1
            pointer = pointer.next

        pointer = head

        if counter - n == 0:
            head = head.next
            return head

        for i in range(1,counter-n):
            pointer = pointer.next

        pointer.next = pointer.next.next

        return head

        