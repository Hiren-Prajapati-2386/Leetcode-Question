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


        # temp node at head
        temp = head

        while temp:
            kNode = findKthNode(temp,k)
            if kNode is None:
                if prevNode:
                    prevNode.next = temp
                break

            NextNode = kNode.next
            kNode.next = None

            reverseLinkList(temp)

            if(temp == head):
                head = kNode
            else:
                prevNode.next = kNode

            prevNode = temp
            temp = NextNode

        return head







        