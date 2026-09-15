# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# class Solution:
#     def hasCycle(self, head: Optional[ListNode]) -> bool:
#         # use set insterd map becuse serching eliment take o(1) time 
#         seen = set()

#         point = head

#         while(point is not None):
#             if point in seen:
#                 return True
#             seen.add(point)

#             point = point.next

        
#         return False


        # time complecity :- O(n)
        # space complecity is also O(n)  so this is good but not whatleetcode ask


        
class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        # Floyd’s Cycle-Finding Algorithm

        # we have two pointer fast and slow
        fast = head
        slow = head

        while fast is not None and fast.next is not None:

            fast = fast.next.next
            slow = slow.next

            if fast == slow:
                return True

        return False