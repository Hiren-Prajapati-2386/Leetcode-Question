# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:

        seen = set()
        point = headA

        while point is not None:
            seen.add(point)
            point = point.next

        point2 = headB

        while point2 is not None:
            if point2 in seen:
                return point2
            point2 = point2.next

        return None
        