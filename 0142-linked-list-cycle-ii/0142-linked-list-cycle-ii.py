# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# class Solution:
#     def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:

#         # thies solution is brut force take O(n) extra space so we know best solution is Floyd’s Cycle-Finding Algorithm
#         seen = set()

#         point = head

#         while point is not None:
            
#             if point in seen:
#                 return point

#             seen.add(point)

#             point = point.next


#         return None


class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:

        fast = head
        slow = head

        while fast is not None and fast.next is not None:

            fast = fast.next.next
            slow = slow.next

            if fast == slow:
                slow = head
                while(slow != fast):
                    fast = fast.next
                    slow = slow.next

                return slow

        return None