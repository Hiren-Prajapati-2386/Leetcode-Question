class Solution:
    def reverseBetween(self, head: ListNode | None, left: int, right: int) -> ListNode | None:
        if not head or left == right:
            return head

        dummy = ListNode(0)
        dummy.next = head
        prev = dummy

        # move prev to the node right before left
        for _ in range(left - 1):
            prev = prev.next

        # curr is the first node of the segment to reverse
        curr = prev.next

        # repeatedly move curr.next right after prev
        for _ in range(right - left):
            temp = curr.next
            curr.next = temp.next
            temp.next = prev.next
            prev.next = temp

        return dummy.next