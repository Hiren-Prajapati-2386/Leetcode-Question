# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:

    

    def isPalindrome(self, head: ListNode | None) -> bool:

        # first find middle so we can reverse half part 
        # fast and slow approch

        fast = head
        slow = head

        while fast.next and fast.next.next:

            slow = slow.next
            fast = fast.next.next


        def reverse(point: ListNode):
            privNode = None
            while point:
                nextNode = point.next
                point.next = privNode
                privNode = point
                point = nextNode

            return privNode

        
        # now reverse second part from slow.next
        newhead = reverse(slow.next)

        # travels second and first part and compare palidrom or not
        first = head
        second = newhead

        while second:
            if first.val != second.val:
                return False
            first = first.next
            second = second.next

        # again reverse so at end we get linklist same as first without no change
        reverse(newhead)

        return True




        