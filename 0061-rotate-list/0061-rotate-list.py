# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: ListNode | None, k: int) -> ListNode | None:

        if head is None:
            return head

        count = 1
        tail = head
        while tail.next:
            count += 1
            tail = tail.next

        if k % count == 0:
            return head

        tail.next = head

        k = k % count
        point = head
        for i in range(1,count-k):
            point = point.next

        head = point.next
        point.next = None

        return head


        