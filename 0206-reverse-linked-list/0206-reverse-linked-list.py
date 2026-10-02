# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: ListNode | None) -> ListNode | None:

        currPointer = head
        privPointer = None

# here we only reverse connection and linklist automaticaly reverse
        while currPointer:

            nextPointer = currPointer.next
            currPointer.next = privPointer
            privPointer = currPointer
            currPointer  = nextPointer

        return privPointer
        