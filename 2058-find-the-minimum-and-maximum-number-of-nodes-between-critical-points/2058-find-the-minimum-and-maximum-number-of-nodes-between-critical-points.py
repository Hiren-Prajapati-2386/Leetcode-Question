# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def nodesBetweenCriticalPoints(self, head: ListNode | None) -> list[int]:

        # base case handel
        if not head:
            return [-1,-1]



        prev = head
        point = []
        index = 2
        current = head.next

        while current.next:

            # find critical point local minimul
            if current.val < prev.val and current.val < current.next.val:
                point.append(index)
            elif current.val > prev.val and current.val > current.next.val:
                point.append(index)

            prev = current
            current = current.next
            index += 1

        if len(point) < 2:
            return [-1,-1]
        
        max_dist = point[-1] - point[0]

        min_dist = float("inf")

        for i in range(1,len(point)):
            min_dist = min(min_dist, point[i] - point[i - 1])

        return [min_dist,max_dist]


        