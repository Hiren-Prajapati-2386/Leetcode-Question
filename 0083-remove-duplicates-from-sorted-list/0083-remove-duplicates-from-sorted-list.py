# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:

        # code writen by me so try again you can solve it

        if head == None:
            return None

        first = head
        second = head.next

        while(second != None):
            if first.val != second.val:
                first.next = second
                first = first.next
                second = second.next

            else:
                first.next = None
                second = second.next

        return head
        